import { combineReducers } from 'redux';
// 全局reducer
import isLogin from './indexReducer.js'
// 合并reducer
var rootReducer = combineReducers({
	isLogin
});
// export rootReducer
export default rootReducer;
