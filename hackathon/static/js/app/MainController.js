var app = angular.module("main-ctrl", []);

app.controller("MainController", function($scope, GetUser, Processes, Tasks) {
  $scope.data = [
    {
      id: 1,
      title: "node1",
      nodes: [
        {
          id: 11,
          title: "node1.1",
          nodes: [
            {
              id: 111,
              title: "node1.1.1",
              nodes: []
            }
          ]
        },
        {
          id: 12,
          title: "node1.2",
          nodes: []
        }
      ]
    },
    {
      id: 2,
      title: "node2",
      nodrop: true,
      nodes: [
        {
          id: 21,
          title: "node2.1",
          nodes: []
        },
        {
          id: 22,
          title: "node2.2",
          nodes: []
        }
      ]
    },
    {
      id: 3,
      title: "node3",
      nodes: [
        {
          id: 31,
          title: "node3.1",
          nodes: []
        }
      ]
    }
  ];

  // $scope.currentUser = GetUser.query()

  Processes.query().$promise.then(res => {
    $scope.processes = res;
    
    setTimeout(() => {
      var tooltips = document.querySelectorAll('.tooltipped');
      var instances = M.Tooltip.init(tooltips, {
        // html: "<div style='width: 200px'></div>"
      });
    }, 200)
    
  });
  
    
  $scope.openCard = function (card) {
      $scope.selectedCard = card;
      console.log(card)
  }

  /* Get User Organizations */
  // GetUser.get({ pk: 1 }, res => {
  //   console.log(res);
  // })

  // Processes.get({}, res => {
  //   console.log(res);
  // })

  $scope.getDocumentsCount = function (doc_types) {
    if (doc_types) return doc_types.reduce((acc, doc_type) => {
        return acc += doc_type.documents.length;
      }, 0);
    else return 0;
  }

  console.log("main controller");
});
