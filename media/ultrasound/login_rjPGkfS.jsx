import axios from "axios";
import qs from "qs";
import React from "react";
import showPwdImg from "./show-password.svg";
import hidePwdImg from "./hide-password.svg";
import slogo from "../img/sukhprasavamlogo.png";
import { Link } from "react-router-dom";

import { initializeApp } from "firebase/app";
import { getMessaging, getToken } from "firebase/messaging";
// Initialize Firebase
const firebaseConfig = {
  apiKey: "AIzaSyDDrqVCZ7k8JvJMAFcT8QoIcZB5Dd2qBlk",
  authDomain: "shebirth-56315.firebaseapp.com",
  projectId: "shebirth-56315",
  storageBucket: "shebirth-56315.appspot.com",
  messagingSenderId: "863574233401",
  appId: "1:863574233401:web:25894efddd5fc5805058e8",
  measurementId: "G-RYDPEVQEH0",
};
const app = initializeApp(firebaseConfig);

const messaging = getMessaging(app);
// getToken(messaging, {
//   vapidKey:
//     "BNoie0WUfwBNhc3e5K0WXlfjpL0utgNeCOuiESTAigt4RD_6c0ESSjWQY7-nNUodUU0Ql-2jXsLPdoDe_yMrho4",
// });

export default class Form extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      isUser: false,
      username: "",
      password: "",
      items: [],
      isRevealPwd: false,
      fcm_token2: "",
    };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.usernameChange = this.usernameChange.bind(this);
    this.passwordChange = this.passwordChange.bind(this);
  }

  async handleSubmit(e) {
    e.preventDefault();
    const permission = await Notification.requestPermission();
    console.log(permission);
    let currentToken; //
    getToken(messaging, {
      vapidKey:
        "BInjEWhqUD-JZMVN1ClioA8GrKKfcJtg-OQFOigst3agDUVw0LGqxkYu55dir95S4sv8kXZgwpvXqZ9_ZfzfVbM",
    })
      .then((currentToken) => {
        this.setState({ fcm_token2: currentToken });
        console.log("FCM token:", currentToken);
      })
      .catch((error) => {
        console.log("Failed to generate FCM token:", error);
      });
    console.log(this.state.fcm_token2);
    var data = {
      email: this.state.username,
      password: this.state.password,
      fcm_token: this.state.fcm_token2,
    };

    axios({
      method: "POST",
      url: "login/",
      headers: { "content-type": "application/x-www-form-urlencoded" },
      data: qs.stringify(data),
    })
      .then(function (response) {
        console.log("api", response.data);

        if (response.data.client == true) {
          localStorage.setItem("token", response.data.token);
          window.location = "/client";
        } else if (response.data.sales == true) {
          localStorage.setItem("sales", response.data.token);

          localStorage.setItem("token", response.data.token);
          window.location = "/csteam";
        } else if (response.data.consltant == true) {
          localStorage.setItem("token", response.data.token);
          window.location = "/consultant";
        } else if (response.data.doctor == true) {
          localStorage.setItem("doc_token", response.data.token);
          window.location = "/doctor";
        } else if (response.data.dad == true) {
          sessionStorage.setItem("dad", response.data.token);
          window.location = "/dad";
        } else if (response.data.hospitalManager == true) {
          sessionStorage.setItem("hospitalManager", response.data.token);
          window.location = "/hmanager";
        } else {
          alert("User with the email not found!");

          console.log("this is error");
        }
      })
      .catch((error) => {
        console.error(error);
      });
  }

  usernameChange(e) {
    this.setState({ username: e.target.value });
  }

  passwordChange(e) {
    this.setState({ password: e.target.value });
  }
  signup = (e) => {
    // e.preventDefault();
    // localStorage.clear();
    window.location = "/csignup";
  };

  docsignup = (e) => {
    // e.preventDefault();
    // localStorage.clear();
    window.location = "/doc_signup";
  };

  render() {
    return (
      <>
        <div
          className="form-wrapper"
          style={{
            display: "flex",
            flexDirection: "column",
            color: "#fff",
            padding: "20px",
            width: "40%",
            borderRadius: "20px",

            boxShadow: "rgb(0 0 0 / 16%) 12px 10px 60px",
            backdropFilter: "blur(39px)",
            background: "rgba(0, 0, 0, 0.16)",
            // boxShadow: "12px 10px 60px #00000029",
            // backdropFilter: "blur(39px)",
            // WebkitBackdropFilter: "blur(39px)",
            // background: "#00000029",
          }}
        >
          {" "}
          <img className=" marginauto pc-view-hidden" src={slogo} />
          <h3 className="smart">Lets Get Started</h3>
          <form
            className="login-mainform"
            style={{
              display: "flex",
              flexDirection: "column",
              lineHeight: "70px",
            }}
            onSubmit={this.handleSubmit}
          >
            <input
              value={this.state.username}
              onChange={this.usernameChange}
              style={styles.input}
              type="text"
              placeholder="Username"
            />
            {/* <input
              value={this.state.password}
              onChange={this.passwordChange}
              style={styles.input}
              type="password"
              placeholder="Password"
            /> */}
            <div className="pwd-container">
              <input
                value={this.state.password}
                onChange={this.passwordChange}
                style={styles.input}
                type={this.state.isRevealPwd ? "text" : "password"}
                placeholder="Password"
              />
              <img
                title={
                  this.state.isRevealPwd ? "Hide password" : "Show password"
                }
                src={this.state.isRevealPwd ? hidePwdImg : showPwdImg}
                onClick={() =>
                  this.setState((prevState) => ({
                    isRevealPwd: !prevState.isRevealPwd,
                  }))
                }
              />
            </div>
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
              }}
            >
              <div>
                <small style={{ display: "flex", paddingTop: "2px" }}>
                  <input type="checkbox" />
                  <span>Remember Me</span>
                </small>
              </div>
              <div>
                <Link to="/forget">
                  <small>Forgot Password</small>
                </Link>
              </div>
            </div>
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
              }}
            >
              <button
                type="button"
                onClick={this.signup}
                style={{
                  background: "none",
                  border: "1px solid #fff",
                  color: "#fff",
                  width: "102px",
                  borderRadius: "4px",
                  cursor: "pointer",
                }}
              >
                Signup
              </button>
              <input
                style={{
                  background:
                    "transparent linear-gradient(266deg, #FF006C 0%, #293247 100%) 0% 0% no-repeat padding-box",
                  width: "102px",
                  height: "32px",
                  border: "none",
                  color: "#fff",
                  boxShadow: "0px 9px 10px #00000029",
                  borderRadius: "4px",
                  cursor: "pointer",
                }}
                type="submit"
                value="Login"
              />
            </div>
          </form>
        </div>
      </>
    );
  }
}

const styles = {
  input: {
    background: "none",
    padding: "10px",
    color: "#fff",
    borderTop: "none",
    borderLeft: "none",
    borderRight: "none",
  },
};
