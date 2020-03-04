import React from 'react';
import { Route, Switch } from 'react-router-dom';

import Home from 'pages/home';
import Page from 'pages/page';
import Counter from 'pages/counter';

const getRouter = () => (
    <Switch>
        <Route exact path='/' component={Home}/>
        <Route path='/page' component={Page}/>
        <Route path='/counter' component={Counter}/>
    </Switch>
)

export default getRouter;