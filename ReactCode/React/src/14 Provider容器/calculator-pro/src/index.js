import React from 'react';
import ReactDOM from 'react-dom';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import reducerCalculator from './reducers/reducerCalculator';
import { App } from './containers/App';
// TODO: Create Store
const store = createStore(reducerCalculator);
const rootEle = document.getElementById('root');
// TODO: render
const render = () => ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
rootEle
);
// TODO: call render
render();
// TODO: subscribe
store.subscribe(render);
