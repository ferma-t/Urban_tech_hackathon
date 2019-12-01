
  document.addEventListener('DOMContentLoaded', function() {
    var sidenav = document.querySelectorAll('.sidenav');
    var sidenaInstances = M.Sidenav.init(sidenav, { edge: "right"});
    
    // // init tabs
    // var tabs = document.querySelectorAll('.tabs');
    // var tabInstances = M.Tabs.init(tabs, {});
    
    // init dropdown
    var dropdown = document.querySelectorAll('.dropdown-trigger');
    var dropdownInstances = M.Dropdown.init(dropdown, {coverTrigger: false});

    

  });

