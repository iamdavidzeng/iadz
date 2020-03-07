import React from 'react';
import ReactDom from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter as Router } from 'react-router-dom';

import Nav from './components/Nav';
import getRouter from './router';
import store from './redux/store';
import '../mock/mock.js';


ReactDom.render(
    // Provider在根组件外面包了一层，App的所有子组件就默认都可以拿到store，通过组件的props传递
    <Provider store={store}>
        <Router>
            <Nav />
            {getRouter()}
        </Router>
    </Provider>,
    document.getElementById('app')
);
