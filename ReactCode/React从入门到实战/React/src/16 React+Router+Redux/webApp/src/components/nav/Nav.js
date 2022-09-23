import React, { Component } from 'react';
import {
  Route,
  Link
} from 'react-router-dom';
// TODO: Nav Component
class Nav extends Component {
  render() {
    return (
		<ul style={{display:this.props.isLogin?"block":"none"}}>
			<li style={{display:this.props.isLogin?"none":"block"}}>
				<Link to="/">Login</Link>
			</li>
			<li>
				<Link to="/Home">Home</Link>
			</li>
			<li>
				<Link to="/About">About Us</Link>
			</li>
		</ul>
    );
  }
}
// TODO: export Nav
export default Nav;
