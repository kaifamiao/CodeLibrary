import { CalculateType } from '../actions'
// TODO: init state
const initState = {
  n1: '',
  n2: '',
  opr: '',
  eq: '',
  result: ''
};
// TODO: reducer
var reducerCalculator = (state = initState, action) => {
  switch (action.type) {
    case CalculateType.NUM:
      return {
        n1: action.n1,
        n2: action.n2,
        opr: action.opr,
        eq: action.eq,
        result: action.result
      };
    case CalculateType.OPR:
      return {
        n1: action.n1,
        n2: action.n2,
        opr: action.opr,
        eq: action.eq,
        result: action.result
      };
    case CalculateType.EQUALS:
      let result;
      switch(action.opr) {
        case 'add':
          result = Number.parseInt(action.n1) + Number.parseInt(action.n2);
          break;
        case 'minus':
          result = Number.parseInt(action.n1) - Number.parseInt(action.n2);
          break;
        case 'multiple':
          result = Number.parseInt(action.n1) * Number.parseInt(action.n2);
          break;
        case 'divide':
          if(Number.parseInt(action.n2) !== 0) {
            result = Number.parseInt(action.n1) / Number.parseInt(action.n2);
          } else {
            result = Number.NaN;
          }
          break;
        default:
          result = 0;
          break;
      }
      return {
        n1: action.n1,
        n2: action.n2,
        opr: action.opr,
        eq: action.eq,
        result: result
      };
    case CalculateType.CLS:
      return {
        n1: action.n1,
        n2: action.n2,
        opr: action.opr,
        eq: action.eq,
        result: action.result
      };
    default:
      return state;
  }
};
// TODO: export Reducer
export default reducerCalculator;
