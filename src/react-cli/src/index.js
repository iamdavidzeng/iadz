import React from 'react';
import ReactDom from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter as Router } from 'react-router-dom';

import Nav from './components/Nav';
import getRouter from './router';
import store from './redux/store';


ReactDom.render(
    <Provider store={store}>
        <Router>
            <Nav />
            {getRouter()}
        </Router>
    </Provider>,
    document.getElementById('app')
);
