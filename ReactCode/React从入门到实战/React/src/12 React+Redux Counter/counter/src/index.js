import React from 'react';
import ReactDOM from 'react-dom';
import { createStore } from 'redux';
import CounterComp from './components/CounterComp';
import reducerCounter from './reducers/reducerCounter';
// TODO: Create Store
const store = createStore(reducerCounter);
const rootEle = document.getElementById('root');
// TODO: render
const render = () => ReactDOM.render(
  <CounterComp
    value={store.getState()}
    vstore={store}
  />,
  rootEle
);
// TODO: call render
render();
// TODO: subscribe
store.subscribe(render);
