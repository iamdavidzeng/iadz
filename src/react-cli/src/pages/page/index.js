import React, { PureComponent } from 'react';

import style from './index.css';
import pic from 'images/a.jpg';

export default class Home extends PureComponent {
    render() {
        return <div class={style['page-box']}>this is page~<img src={pic}/></div>
    }
}