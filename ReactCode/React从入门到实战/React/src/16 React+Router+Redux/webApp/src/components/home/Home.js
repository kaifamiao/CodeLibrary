import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
// TODO: Home Component
class Home extends Component {
  // TODO: render
	render() {
		if(this.props.isLogin==false){
			return <Redirect to="/" />
		}
		return (
			<div>
        <div>
          <button onClick={this.userLogout.bind(this)}>Logout</button>
        </div>
        <div>
          <h3>Home</h3>
          <p>Hi, this is home page.</p>
        </div>
			</div>
		);
	}
	// TODO: Logout
  userLogout(){
		this.props.LOGOUT(this.props.history);
	}
	// TODO: componentDidMount
	componentDidMount() {
	  	console.log("Home render complete.");
	}
}
// TODO: export
export default Home;
