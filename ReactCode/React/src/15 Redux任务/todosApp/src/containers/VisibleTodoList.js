import { connect } from 'react-redux';
import { toggleTodo } from '../actions';
import TodoList from '../components/TodoList';
import { VisibilityFilters } from '../actions';
// TODO: getVisibleTodos
const getVisibleTodos = (todos, filter) => {
  switch (filter) {
    case VisibilityFilters.SHOW_ALL:
      return todos;
    case VisibilityFilters.SHOW_COMPLETED:
      return todos.filter(t => t.completed);
    case VisibilityFilters.SHOW_ACTIVE:
      return todos.filter(t => !t.completed);
    default:
      throw new Error('Unknown filter: ' + filter);
  }
}
// TODO: mapStateToProps
const mapStateToProps = state => ({
  todos: getVisibleTodos(state.todos, state.visibilityFilter)
});
// TODO: mapDispatchToProps
const mapDispatchToProps = dispatch => ({
  toggleTodo: id => dispatch(toggleTodo(id))
});
// TODO: export
export default connect(
  mapStateToProps,
  mapDispatchToProps
)(TodoList);
