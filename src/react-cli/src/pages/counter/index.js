import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import { increment, decrement, reset } from 'actions/counter';

class Counter extends PureComponent {
    render() {
        // View的状态来自于props，props传递的是store中的state
        // const { counter, increment, decrement, reset } = this.props;
        return (
            <div>
                <div>当前计数为{this.props.count}</div>
                <button onClick={() => this.props.increment()}>自增</button>
                <button onClick={() => this.props.decrement()}>自减</button>
                <button onClick={() => this.props.reset()}>重置</button>
            </div>
        )
    }
}

export default connect(
    state => ({
        count: state.counter.count
    }), //  输入，将store中的state通过props输入
    dispatch => ({  //  输出，将action作为props绑定到View上，用户操作类型在此分发出去
        increment: () => {
            dispatch(increment())
        },
        decrement: () => {
            dispatch(decrement())
        },
        reset: () => {
            dispatch(reset())
        },
    })
)(Counter);