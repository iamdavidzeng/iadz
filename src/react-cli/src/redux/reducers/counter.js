import { INCREMENT, DECREMENT, RESET } from 'actions/counter';

/*
* 初始化state
 */
const initState = {
    count: 0
}

/*
* reducer
 */
// 通过判断Action的类型，返回新的数据改变后的state对象，即使没有任何状态的改变，也要返回一个对象
export default function reducer(state=initState, action) {
    switch (action.type) {
        case INCREMENT:
            return {
                count: state.count + 1
            };
        case DECREMENT:
            return {
                count: state.count - 1
            };
        case RESET:
            return {count: 0};
        default:
            return state
    }
}