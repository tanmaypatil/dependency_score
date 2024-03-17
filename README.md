# dependency score calculation
Dependency score calculation for software project
Quite often in a software product developed by a large organisation will have a inter team dependencies . Following teams are in focus
* Team which develops application , focuses on functional aspects
* Infra team which provides infrastructure such as security , authentication , resilliency 
* Devops team which provides access to resources such as kubernetes cluster , IDP's , active directory etc.

Quite often application development team gets stuck because of dependencies on infra and devops team .  During development time , stakeholders are looking for input on the epics and requirement which has higher dependency on other teams .  This is an attempt to look at calculating dependency of a epic. 

