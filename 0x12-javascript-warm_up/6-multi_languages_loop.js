#!/usr/bin/node
const languages = ["C", "Python", "JavaScript"];
for (let i = 0; i < languages.length; i++) {
  console.log(languages[i] + " is " +
    (i === 0 ? "fun" : i === 1 ? "cool" : "amazing"));
}
