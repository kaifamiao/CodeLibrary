import { connect } from 'react-redux';
import { setVisibilityFilter } from '../actions';
import Link from '../components/Link';
// TODO: mapStateToProps
const mapStateToProps = (state, ownProps) => ({
  active: ownProps.filter === state.visibilityFilter
});
// TODO: mapDispatchToProps
const mapDispatchToProps = (dispatch, ownProps) => ({
  onClick: () => dispatch(setVisibilityFilter(ownProps.filter))
});
// TODO: export
export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Link);
