import { createStore } from "vuex";
import axios from "axios";

const state = {
  user: {
    name: "",
    img: "",
  },
  sessions: [],
  currentSessionId: 1,
  filterKey: "",
  socket: null,
};

const mutations = {
  INIT_DATA(state, { username, onlineUsers }) {
    if (typeof WebSocket === "undefined") {
      console.log("WebSocket is not supported by your browser.");
      return;
    } else {
      console.log("WebSocket is supported by your browser.");

      document.cookie = "user=" + username;
      state.socket = new WebSocket("ws://localhost:8080/ws");

      state.socket.onopen = function () {
        console.log("connected");
        // set user info and display online users.
        state.user = { name: username, img: username + ".jpeg" };
        if (onlineUsers.length > 0) {
          onlineUsers.forEach((username) => {
            if (username != state.user.name) {
              state.sessions.push({
                id: state.sessions.length + 1,
                user: {
                  name: username,
                  img: username + ".jpeg",
                },
                messages: [],
              });
            }
          });
        }
      };

      state.socket.onmessage = function (msg) {
        let data = JSON.parse(msg.data);
        let session = state.sessions.find((s) => s.user.name === data.from);

        // if session not found, create new session for the sender.
        if (!session) {
          const id = state.sessions.length + 1;
          state.sessions.push({
            id,
            user: {
              name: data.from,
              img: data.from + ".jpeg",
            },
            messages: [],
          });
          session = state.sessions.find((s) => s.id === id);
        }
        // if sender leaves the chat, remove the session.
        if (session && data.content.includes("left the group")) {
          state.sessions = state.sessions.filter((s) => s.id !== session.id);
        }
        // if sender sends a message, add the message to the session.
        if (!data.content.includes("joined the group")) {
          session.messages.push({
            content: data.content,
            date: new Date(),
            self: false,
          });
        }
      };

      state.socket.onerror = function () {
        state.socket.close();
        state.socket = null;
      };
    }
  },
  SEND_MESSAGE({ sessions, currentSessionId }, content) {
    var session = sessions.find((s) => s.id === currentSessionId);
    if (session) {
      state.socket.send(
        JSON.stringify({
          from: state.user.name,
          to: session.user.name,
          content: content,
          channel_type: "user",
        })
      );
      session.messages.push({
        content: content,
        date: new Date(),
        self: true,
      });
    }
  },
  SELECT_SESSION(state, id) {
    state.currentSessionId = id;
  },
  SELF_FILTER_KEY(state, key) {
    state.filterKey = key;
  },
  CLOSE_SOCKET(state) {
    if (state.socket) {
      state.socket.close();
    }
  },
};

const actions = {
  async initData({ commit }, username) {
    const response = await axios.get("http://localhost:8080/api/users");
    commit("INIT_DATA", { username, onlineUsers: response.data });
  },
  sendMessage({ commit }, content) {
    commit("SEND_MESSAGE", content);
  },
  selectSession({ commit }, id) {
    commit("SELECT_SESSION", id);
  },
  search({ commit }, key) {
    commit("SELF_FILTER_KEY", key);
  },
  closeSocket({ commit }) {
    commit("CLOSE_SOCKET");
  },
};

export const store = createStore({
  state,
  actions,
  mutations,
});
