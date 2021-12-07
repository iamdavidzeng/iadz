import { createStore } from 'vuex';

const now = new Date();
const state = {
    user: {
        name: 'david',
        img: 'david.jpeg',
    },
    sessions: [
        {
            id: 1,
            user: {
                name: 'lucy',
                img: 'lucy.jpeg',
            },
            messages: [
                {
                    content: 'foo',
                    date: now,
                },
                {
                    content: 'bar',
                    date: now,
                }
            ]
        }
    ],
    currentSessionId: 1,
    filterKey: '',
};

const mutations = {
    INIT_DATA(state) {
        let data = localStorage.getItem('vite-chat-session');
        console.log(data);
        if (data) {
            state.sessions = JSON.parse(data);
        }
    },
    SEND_MESSAGE({ sessions, currentSessionId }, content) {
        let session = sessions.find(s => s.id === currentSessionId);
        session.messages.push({
            content: content,
            date: new Date(),
            self: true,
        });
    },
    SELECT_SESSION(state, id) {
        state.currentSessionId = id;
    },
    SELF_FILTER_KEY(state, key) {
        state.filterKey = key;
    },
};

const actions = {
    initData({ commit }) {
        commit('INIT_DATA');
    },
    sendMessage({ commit }, content) {
        commit('SEND_MESSAGE', content);
    },
    selectSession({ commit }, id) {
        commit('SELECT_SESSION', id);
    },
    search({ commit }, key) {
        commit('SELF_FILTER_KEY', key);
    },
};

export const store = createStore({
    state,
    actions,
    mutations
});
