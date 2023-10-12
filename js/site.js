var ChatApp = window.ChatApp || {};

(function () {
    var userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);
    var token = null;
    var lastChat = null;
    var apiClient = apigClientFactory.newClient();

    ChatApp.checkLogin = function (redirectOnRec, redirectOnUnrec) {
        var cognitoUser = userPool.getCurrentUser();
        if (cognitoUser !== null) {
            if (redirectOnRec) {
                window.location = '/chats.html';
            }
        } else {
            if (redirectOnUnrec) {
                window.location = '/';
            }
        }
    };

    ChatApp.login = function () {
        var username = $('#username').val();
        var password = $('#password').val();
        authenticateUser(username, password);
    };

    ChatApp.logout = function () {
        signOutUser();
    };

    ChatApp.populateChats = function () {
        getTokenAndPopulateChats();
    };

    ChatApp.loadChat = function () {
        getTokenAndLoadChat();
    };

    ChatApp.send = function () {
        sendMessage();
    };

    ChatApp.populatePeople = function () {
        getTokenAndPopulatePeople();
    };

    ChatApp.startChat = function (name) {
        startConversation(name);
    };

    ChatApp.signup = function () {
        var username = $('#username').val();
        var password = $('#password').val();
        var email = $('#email').val();
        signUpUser(username, password, email);
    };

    ChatApp.confirm = function () {
        var code = $('#code').val();
        confirmRegistration(code);
    };

    ChatApp.resend = function () {
        resendConfirmationCode();
    };

    function authenticateUser(username, password) {
        var authenticationData = {
            Username: username,
            Password: password
        };

        var authenticationDetails = new AmazonCognitoIdentity.AuthenticationDetails(authenticationData);
        var userData = {
            Username: username,
            Pool: userPool
        };
        var cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);

        cognitoUser.authenticateUser(authenticationDetails, {
            onSuccess: function () {
                window.location = '/chats.html';
            },
            onFailure: function (err) {
                alert(err);
            }
        });
    }

    function signOutUser() {
        var cognitoUser = userPool.getCurrentUser();
        cognitoUser.signOut();
        window.location = '/';
    }

    function getTokenAndPopulateChats() {
        getToken(function (token) {
            apiClient.conversationsGet({}, null, {headers: {Authorization: token}})
                .then(function (result) {
                    var currentUsername = userPool.getCurrentUser().getUsername();

                    result.data.forEach(function (convo) {
                        // Populate chats here
                        // ...
                    });
                });
        });
    }

    function getTokenAndLoadChat() {
        getToken(function (token) {
            // Load chat here
            // ...
        });
    }

    function sendMessage() {
        getToken(function (token) {
            // Send message here
            // ...
        });
    }

    function getTokenAndPopulatePeople() {
        getToken(function (token) {
            // Populate people here
            // ...
        });
    }

    function startConversation(name) {
        getToken(function (token) {
            // Start conversation here
            // ...
        });
    }

    function signUpUser(username, password, email) {
        // Sign up user here
        // ...
    }

    function confirmRegistration(code) {
        // Confirm registration here
        // ...
    }

    function resendConfirmationCode() {
        // Resend confirmation code here
        // ...
    }

    function getToken(callback) {
        if (token === null) {
            var cognitoUser = userPool.getCurrentUser();
            if (cognitoUser !== null) {
                cognitoUser.getSession(function (err, session) {
                    if (err) {
                        window.location = '/';
                    }
                    token = session.getIdToken().getJwtToken();
                    callback(token);
                });
            }
        } else {
            callback(token);
        }
    }
})();
