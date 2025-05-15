**#CI/CD with Jenkins for Network Automation**
This project is part of the Network Management and Automation course offered by the University of Colorado Boulder's Network Engineering Program. The goal of this lab is to build a Jenkins-based CI/CD pipeline to automate network configuration deployment using Infrastructure-as-Code (IaC) practices.

**#Project Objectives**
Understand the core functionalities of Jenkins.
Integrate Jenkins with GitHub for version control and automated triggers.
Develop a multi-stage Jenkins pipeline to manage Python-based network scripts.
Validate code quality using PEP8 standards with pylint.
Run unit tests to verify network configurations before deployment.
Configure GitHub webhooks to enable automatic job triggering.
Set up email notifications to report job outcomes.
Schedule nightly builds to ensure continuous integration.

**#Tools and Technologies**
Jenkins
GitHub
Python (including unittest, pylint, ncclient, pandas, etc.)
Netconf over SSH with Cisco routers (via GNS3)
Ngrok for webhook tunneling
Jenkins email notification system

**#Repository Contents**
Jenkinsfile: Defines the pipeline structure and stages.
netman_netconf_obj2.py: Python script that configures network devices.
info.csv: CSV file containing router interface data.
test_netconf.py: Unit test script to verify configuration outcomes.

**#Unit Testing Scenarios**
Confirm that loopback 99 on Router 3 is configured with IP 10.1.3.1/24.
Validate that Router 1 is configured with a single OSPF area.
Ensure that a ping from Router 2’s loopback to Router 5’s loopback is successful.

**#Features**
Automated job triggering on GitHub commits using webhooks.
Quality gate enforcement with code style checks.
Email notifications for build success or failure.
Nightly job scheduling for ongoing code validation and integration testing.
