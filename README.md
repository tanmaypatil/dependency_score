# Dependency score calculation
## Background
Dependency score calculation for software project
Software product developed by a large organisation  have  inter team dependencies . These dependencies stall the flow.  
Following teams are the actors in a cross team collaborated product
* Team which develops application , focuses on functional aspects
* Infra team which provides infrastructure such as security , authentication , resilliency 
* Devops team which provides access to resources such as kubernetes cluster , IDP's , active directory etc.

Application development team gets stuck because of dependencies on infra and devops team . 
During execution , stakeholders (such as program managers, engineering directors ) are looking for input on the epics and requirement which has higher dependency on other teams .  This is an attempt to look at calculating dependency of a epic. 

## How to calculate score  
Current method of implementation is to use weighted score of following parameters to arrive at dependency score 
* Requirement effort - 10% weightage 
* Dependency effort - 10 % weightage
* Product priority - 50% weightage
* Sprint arrival - 30% weightage

### Score calculation - input scaling
All the input variables ( such as requirement effort) is scaled to value between 1 and 5 so as to have uniformity . Final dependency score would between less than 5 . 
Higher the score and higher the dependency of a requirement or epic on other teams 

### Variables 
* Requirement effort 
Effort in person days of the epic under question . It could be between 0 to 200 person days .
Lower and upper bounds are configurable . This value is scaled down to be between 0 to 5.




