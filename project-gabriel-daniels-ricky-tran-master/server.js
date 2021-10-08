//Ricky Tran (1832920)
//Gabriel Daniels (1856516)

// load the things we need
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');

// required module to make calls to a REST API
const axios = require('axios');
const { request } = require('express');

// parses out incoming requests bodies before being used in actual code
app.use(bodyParser.urlencoded());

// set the view engine to ejs
app.set('view engine', 'ejs');

// use res.render to load up an ejs view file

// about page
app.get('/about', function(req, res) {

    //local API call to my Python REST API that delivers cars
    axios.get(`http://127.0.0.1:5000/api/friends/all`)
    .then((response)=>{
        
        var friend = response.data;
        var tagline = "Here is the data coming from my own API";
        console.log(friend);
         // use res.render to load up an ejs view file
        res.render('pages/about', {
            friends: friend,
            tagline: tagline
        });
    });    
});

// Home page
app.get('/', function(req, res) {
  var addfVar = "Javascript";
  
  // this will render our home page 
  res.render("pages/index.ejs", {addfVar: addfVar});
});

//loads addfriend form
app.get('/addfriend', function(req, res) {
  var addfVar = "Javascript";
  
  // this will render our new addfriend page 
  res.render("pages/addfriend.ejs", {addfVar: addfVar});
});

// gets info from addfriend form to be used later
app.post('/add_friend', function(req, res){
    var firstname = req.body.firstname;
    var lastname = req.body.lastname;
    
    console.log(firstname);
    axios.post('http://127.0.0.1:5000//api/addfriend', {
        id: 5000,
        firstname: firstname,
        lastname: lastname
      })
      .then(function (response) {
        console.log(reponse.data);
      })

      res.render('pages/thanks.ejs', {body: req.body.firstname + " has been added successfully!"})
});

// loads deletes friend form
app.get('/delfriend', function(req, res) {
  var delfVar = "Javascript";
  
  // this will render our new addf spage 
  res.render("pages/delfriend.ejs", {delfVar: delfVar});
});

// gets info from user to delete friend from tables
app.post('/del_friend', function(req, res){
    var friendid = req.body.friendid;
    var firstname = req.body.firstname;
    var lastname = req.body.lastname;
    
    console.log(firstname);
    axios.post('http://127.0.0.1:5000//api/delfriend', {
        id: 5000,
        friendid: friendid,
        firstname: firstname,
        lastname: lastname
      })
      .then(function (response) {
        console.log(reponse.data);
      })

      res.render('pages/thanks.ejs', {body: req.body.firstname + " has been deleted successfully! Check the Friend List to ensure they have been removed"})
});

// loads addmovie form
app.get('/addmovie', function(req, res) {
  var addmVar = "Javascript";
  
  // this will render our new addf spage 
  res.render("pages/addmovie.ejs", {addmVar: addmVar});
});

// loads findid form
app.get('/findid', function(req, res) {
  var find = "Javascript";
  
  // this will render our new addf spage 
  res.render("pages/findid.ejs", {find: find});
});

// gets all friends from sql table
app.get('/allfriend', function(req, res) {
  axios.get(`http://127.0.0.1:5000/api/friends/all`)
  .then((response)=>{
      
      var friend = response.data;
      var tagline = "Ticket #, First Name, Last Name";
      console.log(friend);
       // use res.render to load up an ejs view file
      res.render('pages/allfriend', {
          friend: friend,
          tagline: tagline
      });
  }); 
});

// loads addmovie form and allows user to input movies for certain friend
app.post('/add_movie', function(req, res){
  var friendid = req.body.friendid;
  var movie1 = req.body.movie1;
  var movie2 = req.body.movie2;
  var movie3 = req.body.movie3;
  var movie4 = req.body.movie4;
  var movie5 = req.body.movie5;
  var movie6 = req.body.movie6;
  var movie7 = req.body.movie7;
  var movie8 = req.body.movie8;
  var movie9 = req.body.movie9;
  var movie10 = req.body.movie10;
  
  console.log(friendid);
  axios.post('http://127.0.0.1:5000//api/addmovie', {
      id: 5000,
      friendid: friendid,
      movie1: movie1,
      movie2: movie2,
      movie3: movie3,
      movie4: movie4,
      movie5: movie5,
      movie6: movie6,
      movie7: movie7,
      movie8: movie8,
      movie9: movie9,
      movie10: movie10
    })
    .then(function (response) {
      console.log(reponse.data);
    })
    var body = "Movie(s)"
    res.render('pages/thanks.ejs', {body: body + "  has been added successfully!"})
});

// shows random movie after function is ran
app.get('/getmovie', function(req, res) {
  axios.get(`http://127.0.0.1:5000/api/random`)
  .then((response) =>{
    var movies = response.data;
    var movie = (movies[0][0])
    var tag = "Looks like y'all are watching..."
    console.log(movie)
    res.render('pages/getmovie', {
      movie: movie,
      tag: tag
    });
  });
});

app.listen(1090);
console.log('1090 is the magic port');
