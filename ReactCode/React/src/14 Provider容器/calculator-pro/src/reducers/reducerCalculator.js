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
      console.log('action:' + action);
      switch(action.opr) {
        case 'add':
          return {
            n1: action.n1,
            n2: action.n2,
            opr: action.opr,
            eq: action.eq,
            result: Number.parseInt(action.n1) + Number.parseInt(action.n2)
          };
        case 'minus':
          return {
            n1: action.n1,
            n2: action.n2,
            opr: action.opr,
            eq: action.eq,
            result: Number.parseInt(action.n1) - Number.parseInt(action.n2)
          };
        case 'multiple':
            return {
              n1: action.n1,
              n2: action.n2,
              opr: action.opr,
              eq: action.eq,
              result: Number.parseInt(action.n1) * Number.parseInt(action.n2)
          };
        case 'divide':
          if(Number.parseInt(action.n2) !== 0) {
            return {
              n1: action.n1,
              n2: action.n2,
              opr: action.opr,
              eq: action.eq,
              result: Number.parseInt(action.n1) / Number.parseInt(action.n2)
            }
          } else {
            return {
              n1: action.n1,
              n2: action.n2,
              opr: action.opr,
              eq: action.eq,
              result: Number.NaN
            }
          }
        default:
          return {
            n1: action.n1,
            n2: action.n2,
            opr: action.opr,
            eq: action.eq,
            result: 0
          }
      }
    case CalculateType.CLS:
      return {
        n1: '',
        n2: '',
        opr: '',
        eq: '',
        result: ''
      };
    default:
      return state;
  }
};
// TODO: export Reducer
export default reducerCalculator;
