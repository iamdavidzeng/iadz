<script>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import Card from "./components/Card.vue";
import List from "./components/List.vue";
import Text from "./components/Text.vue";
import Message from "./components/Message.vue";
import Login from './components/Login.vue';
import { mapActions, mapState } from "vuex";

export default {
  components: {
    Card,
    List,
    Text,
    Message,
    Login,
  },
  methods: {
    ...mapActions(["initData", "closeSocket"]),
  },
  computed: {
    ...mapState(["user"]),
  }
};
</script>

<template>
  <div id="app" v-if="user.name">
    <div class="sidebar">
      <Card />
      <List />
    </div>
    <div class="main">
      <Message />
      <Text />
    </div>
  </div>
  <div id="app" v-else>
    <Login />
  </div>
</template>

<style lang="less" scoped>
#app {
  margin: 20px auto;
  width: 800px;
  height: 600px;
  overflow: hidden;
  border-radius: 3px;
  .sidebar,
  .main {
    height: 100%;
  }
  .sidebar {
    float: left;
    width: 200px;
    color: #f4f4f4;
    background-color: #2e3238;
  }
  .main {
    position: relative;
    overflow: hidden;
    background-color: #eee;
  }
  .text {
    position: absolute;
    width: 100%;
    bottom: 0;
    left: 0;
  }
  .message {
    height: ~"calc(100% - 160px)";
  }
}
</style>
