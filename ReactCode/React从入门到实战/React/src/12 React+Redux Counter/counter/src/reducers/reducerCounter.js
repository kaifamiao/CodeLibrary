import { CounterType } from '../actions'
// TODO: reducer
var reducerCounter = (state = 0, action) => {
  switch (action.type) {
    case CounterType.INCREMENT:
      return state + 1;
    case CounterType.DECREMENT:
      return state - 1;
    case CounterType.DOUBLE:
      return state * 2;
    default:
      return state;
  }
};
// TODO: export Reducer
export default reducerCounter;
