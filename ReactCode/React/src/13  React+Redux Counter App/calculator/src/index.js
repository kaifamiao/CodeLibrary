import React from 'react';
import ReactDOM from 'react-dom';
import { createStore } from 'redux';
import CalculatorComp from './components/CalculatorComp';
import reducerCalculator from './reducers/reducerCalculator';
// TODO: Create Store
const store = createStore(reducerCalculator);
const rootEle = document.getElementById('root');
// TODO: render
const render = () => ReactDOM.render(
  <CalculatorComp
    s={store.getState()}
    vstore={store}
  />,
  rootEle
);
// TODO: call render
render();
// TODO: subscribe
store.subscribe(render);
