---
title: "RPNC"
layout: textlay
excerpt: "AWSG -- RPNC"
sitemap: false
permalink: /rpnc.html
---

# Real-time Physical-layer Network Coding

## Overview

<img src="{{ site.url }}{{ site.baseurl }}/images/respic/pncRelay.png" class="img-responsive" width="50%"/>

Physical-layer Network Coding (PNC) is a technique to exploit wireless interference by turning the supercomposed EM waves into useful network-coded information. In a two-way relay network (TWRN) in which two end nodes communicate via a relay node (e.g., two ground stations communicating via a satellite), allowing the two end nodes to transmit simultaneously and applying PNC at the relay can boost capacity by 100%.

We have implemented a real-time prototype on <a href="http://www.ettus.com/">USRP/GNURadio</a> software-defined platform. We used USRP N210 and the SBX daugherboard. The key features are as follows:

* OFDM-based (with parameters similar to 802.11);
* Support BPSK and Convolutional Code;
* Support hard/soft XOR-CD channel decoder;
<!-- * Use beacons to coordinate simultaneous transmissions; -->
<!-- * Use burst mode to improve the MAC-layer throughput; -->

A demo on the prototype can be found <a href="http://youtu.be/HmRBm_IIBQQ">here</a>.

------------------

## Downloads

This software is **free** for non-commercial academic research and education purposes, but registration (free of charge) is required. Please give us an email to register and request for download. We will send you the source code once we receive your request.

The request form can be found [here](downloads/rpnc-code-request-form.pdf).

Click [here](mailto:jiaxin@ie.cuhk.edu.hk) to contact us.

------------------

## Publications

Our software is basically free. The only requirement is as follow: once you have received our program, you agree to cite our background papers below in the event that your work based upon our work results in publications or other research outputs.

<div class="card">
<div class="card-body">
    L. Lu, T. Wang, S. C. Liew, and S. Zhang
    Implementation of Physical-Layer Network Coding
    Elsevier Physical Communication, vol. 6, no. 1, pp. 74-87, Mar. 2013

    L. Lu, L. You, Q. Yang, T. Wang, M. Zhang, S. Zhang, and S. C. Liew
    Real-time Implementation of Physical-Layer Network Coding
    in ACM SIGCOMM SRIF Workshop, 2013
</div>
</div>
