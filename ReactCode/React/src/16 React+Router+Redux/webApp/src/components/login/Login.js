import React, { Component } from 'react';
// TODO: Login Component
class Login extends Component {
  // TODO: render
  render() {
    return (
      <div>
        <h3>Login Page</h3>
        <div>
          Username:&nbsp;&nbsp;<input type="text" ref="username" />
        </div>
        <div>
          Password:&nbsp;&nbsp;<input type="password" ref="password" />
        </div>
        <div>
          <button onClick={this.userLogin.bind(this)}>Login</button>
        </div>
      </div>
    );
  }
  // TODO: goLogin
  userLogin() {
    this.props.LOGIN(this.refs.username.value, this.refs.password.value, this.props.history);
  }
  // TODO: componentDidMount
  componentDidMount() {
    console.log("Login render complete.");
  }
}
// TOOD: export Login
export default Login;
