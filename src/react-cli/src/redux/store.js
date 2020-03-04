import { createStore } from 'redux';
import counter from 'reducers/counter';

let store = createStore(counter);

export default store;