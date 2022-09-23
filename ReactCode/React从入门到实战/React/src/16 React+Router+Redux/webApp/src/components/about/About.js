import React, { Component } from 'react';
import {
  Redirect,
  Switch,
  Link,
  Route
} from 'react-router-dom';
// TODO: About Component
class About extends Component {
  // TODO: render
	render() {
		if(this.props.isLogin==false){
			return <Redirect to="/" />
		}
		return (
			<div>
				<h3>About Us.</h3>
        <p>Welcome to my react+redux+router website!</p>
			</div>
		);
	}
	componentDidMount() {
	  	console.log("About render complete.");
	}
}
// TODO: export About
export default About;
