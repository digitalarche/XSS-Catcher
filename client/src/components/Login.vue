<template>
  <b-container>
    <b-row>
      <b-col>
        <b-img height="200px" src="/logo.png" />
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-img height="50px" src="/title.png" />
      </b-col>
    </b-row>
    <br />
    <b-row align-v="center">
      <b-col md="4" offset-sm="4">
        <b-card>
          <b-form @submit="postLogin">
            <b-form-group
              id="input-group-username"
              label="Username:"
              label-for="input-field-username"
            >
              <b-form-input
                id="input-field-username"
                v-model="form.username"
                required
                placeholder="Enter username"
              ></b-form-input>
            </b-form-group>
            <b-form-group
              id="input-group-password"
              label="Password:"
              label-for="input-field-password"
            >
              <b-form-input
                type="password"
                id="input-field-password"
                v-model="form.password"
                required
                placeholder="Enter password"
              ></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-remember">
              <b-form-checkbox-group v-model="form.remember" id="input-field-remember">
                <b-form-checkbox v-model="form.remember">Remember me:</b-form-checkbox>
              </b-form-checkbox-group>
            </b-form-group>
            <b-button type="submit" variant="outline-info">Login</b-button>
          </b-form>
        </b-card>
      </b-col>
    </b-row>
    <ChangePassword />
  </b-container>
</template>

<script>
import axios from "axios";

import ChangePassword from "./ChangePassword";

axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded";

const basePath = "/api";

export default {
  components: {
    ChangePassword,
  },
  data() {
    return {
      form: {
        username: "",
        password: "",
        remember: [],
      },
      user: {},
      show_password_modal: false,
    };
  },
  methods: {
    loginProcess() {
      const path = basePath + "/user";
      axios
        .get(path)
        .then((response) => {
          this.user = response.data;
          if (this.user.first_login) {
            this.show_password_modal = true;
          } else {
            this.$router.push({
              name: "Index",
            });
          }
        })
        .catch((error) => {
          if (error.response.status === 401) {
            this.$router.push({ name: "Login" });
          }
        });
    },
    postLogin(evt) {
      evt.preventDefault();
      const path = basePath + "/auth/login";
      var payload = new URLSearchParams();

      payload.append("username", this.form.username);
      payload.append("password", this.form.password);
      payload.append("remember", this.form.remember);

      axios
        .post(path, payload)
        .then((response) => {
          this.makeToast(response.data.detail, "success", response.data.status);
          this.loginProcess();
        })
        .catch((error) => {
          this.form.password = "";
          this.makeToast(
            error.response.data.detail,
            "danger",
            error.response.data.status
          );
        });
    },
    isAuth() {
      const path = basePath + "/user";
      axios
        .get(path)
        .then((response) => {
          void response;
          this.$router.push({
            name: "Index",
          });
        })
        .catch((error) => {
          void error;
        });
    },
    makeToast(message, variant, title) {
      this.$root.$bvToast.toast(message, {
        title: title,
        autoHideDelay: 5000,
        appendToast: false,
        variant: variant,
      });
    },
  },
  created() {
    this.isAuth();
  },
};
</script>

<style>
</style>
