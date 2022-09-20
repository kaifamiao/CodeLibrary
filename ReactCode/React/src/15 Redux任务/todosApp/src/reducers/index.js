import { combineReducers } from 'redux';
import todos from './todos';
import visibilityFilter from './visibilityFilter';
// TODO: export
export default combineReducers({
  todos,
  visibilityFilter
});
