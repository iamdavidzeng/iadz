import React from 'react';
import loadable from 'react-loadable';
import { Route, Switch } from 'react-router-dom';

import Loading from 'components/Loading';

const Home = loadable({
    loader: () => import('pages/Home'),
    loading: Loading,
    timeout: 10000, // 10 seconds
})
const Page = loadable({
    loader: () => import('pages/page'),
    loading: Loading,
    timeout: 10000, // 10 seconds
})
const Counter = loadable({
    loader: () => import('pages/counter'),
    loading: Loading,
    timeout: 10000, // 10 seconds
})
const UserInfo = loadable({
    loader: () => import('pages/userInfo'),
    loading: Loading,
    timeout: 10000,
})

const getRouter = () => (
    <Switch>
        <Route exact path='/' component={Home}/>
        <Route path='/page' component={Page}/>
        <Route path='/counter' component={Counter}/>
        <Route path='/userinfo' component={UserInfo}/>
    </Switch>
)

export default getRouter;