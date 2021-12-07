import { createApp } from 'vue'
import { store } from './store';
import App from './App.vue'

const app = createApp(App);
store.watch(
    (state) => state.sessions,
    (val) => {
        console.log('CHANGE: ', val);
        localStorage.setItem('vue-chat-session', JSON.stringify(val));
    },
    {
        deep: true
    }
);

app.use(store);

app.mount('#app');
