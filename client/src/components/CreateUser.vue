<template>
  <b-modal
    ref="createUserModal"
    id="create-user-modal"
    title="Create user"
    hide-footer
    @hide="cleanup"
  >
    <b-form @submit="createUser" @reset="cleanup">
      <b-form-group
        id="input-group-username"
        label="Username:"
        label-cols="3"
        label-for="input-field-username"
      >
        <b-form-input v-model="username" id="input-field-username"></b-form-input>
      </b-form-group>
      <div class="text-right">
        <b-button type="submit" variant="outline-info">Create user</b-button>
        <b-button type="reset" variant="outline-secondary">Cancel</b-button>
      </div>
    </b-form>
    <b-modal
      ref="viewPasswordModal"
      id="view-password-modal"
      title="User created"
      hide-footer
      @hide="cleanup"
    >
      <p>Username: {{ username }}</p>
      <p>Password: {{ data.detail }}</p>
      <div class="text-right">
        <b-button
          @click="$refs.createUserModal.hide()"
          type="reset"
          variant="outline-secondary"
        >Close</b-button>
      </div>
    </b-modal>
  </b-modal>
</template>

<script>
import axios from "axios";

axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded";

const basePath = "/api";

export default {
  data() {
    return {
      data: {},
      username: "",
    };
  },
  methods: {
    createUser(evt) {
      evt.preventDefault();

      const path = basePath + "/user/new";

      var payload = new URLSearchParams();

      payload.append("username", this.username);

      axios
        .post(path, payload)
        .then((response) => {
          this.data = response.data;
          this.$refs.viewPasswordModal.show();
        })
        .catch((error) => {
          if (error.response.status === 401) {
            this.$router.push({ name: "Login" });
          } else {
            this.makeToast(
              error.response.data.detail,
              "danger",
              error.response.data.status
            );
          }
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
    cleanup() {
      this.data = {};
      this.username = "";
      this.$refs.createUserModal.hide();
      this.$parent.$parent.$parent.getUsers();
    },
  },
};
</script>

<style></style>
