<template>
  <div class="container">
    <input
      type="text"
      v-model="username"
      placeholder="Username"
      class="input"
    />
    <button @click="initData(username)" class="btn">Login</button>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "Login",
  data() {
    return {
      username: "",
    };
  },
  methods: {
    ...mapActions(["initData"]),
  },
};
</script>

<style lang="less" scoped>
.container {
  margin: 20px auto;
  padding: 10px;
  width: 300px;
  height: 100px;
  background-color: #fff;
  border-radius: 5px;
}
input {
  padding: 12px 0;
  margin-bottom: 10px;
  border-radius: 3px;
  border: 2px solid transparent;
  text-align: center;
  width: 50%;
  font-size: 16px;
  transition: border 0.2s, background-color 0.2s;
  background-color: #ecf0f1;
}
.btn {
  background-color: #3498db;
  color: #fff;
  line-height: 25px;
  cursor: pointer;
  width: 50%;
  text-align: center;
}
</style>