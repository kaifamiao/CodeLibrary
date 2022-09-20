import { connect } from 'react-redux';
import Nav from '../components/nav/Nav.js'
// TODO: mapStateToProps
function mapStateToProps(state) {
	return {
		isLogin:state.isLogin
	}
}
// TODO: mapDispatchToProps
function mapDispatchToProps(dispatch) {
	return {};
}
// TODO: connect
var NavReactReducer = connect(
  mapStateToProps,
  mapDispatchToProps
)(Nav);
// TODO: export
export default NavReactReducer;
