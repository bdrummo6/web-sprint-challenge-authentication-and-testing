
const bcrypt = require('bcryptjs');

exports.seed = async function(knex) {
   await knex('auth').insert([
      { username: "user-01", password: bcrypt.hashSync('password-01', 14), level: "user" },
      { username: "user-02", password: bcrypt.hashSync("password-02", 14), level: "user" },
      { username: "user-03", password: bcrypt.hashSync('password-03', 14), level: "user" },
      { username: "user-04", password: bcrypt.hashSync("password-04", 14), level: "user" },
      { username: "user-05", password: bcrypt.hashSync('password-05', 14), level: "user" },
   ])
}


