// namespace 表示在全局 state 上的 key
// state 是初始值，在这里是空数组
// reducers 等同于 redux 里的 reducer，接收 action，同步更新 state
export default {
    namespace: 'products',
    state: [
        { name: 'dva', id: 'dva' },
        { name: 'antd', id: 'antd' },
    ],
    reducers: {
        delete(state, { payload: id }) {
            return state.filter(item => item.id !== id);
        },
    },
};