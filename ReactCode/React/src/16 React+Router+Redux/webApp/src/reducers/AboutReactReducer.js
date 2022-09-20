import { connect } from 'react-redux';
import About from '../components/about/About.js';
// TODO: mapDispatchToProps
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
var AboutReactReducer = connect(
  mapStateToProps,
  mapDispatchToProps
)(About);
// TODO: export
export default AboutReactReducer;
