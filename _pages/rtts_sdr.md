---
title: "RTTS-SDR"
layout: textlay
excerpt: "AWSG -- RTTS-SDR"
sitemap: false
permalink: /rtts-sdr.html
---

# Real-time Time-slotted System on SDR

## Overview

<img src="{{ site.url }}{{ site.baseurl }}/images/respic/rtts_sdr.jpg" class="img-responsive" width="50%"/>

RTTS-SDR is a system that we implemented on PC-USRP using GNURadio. It can achieve synchronization among nodes and aligned their time slots to within 100ns, and the end-to-end latency can be down to **3.75ms**.

The prototype is implemented on [USRP/GNURadio](http://www.ettus.com/) software-defined platform. We used USRP X310 and the UBX daugherboard. The key features are as follows:

* OFDM-based (with parameters similar to 802.11);
* Support all bitrates introduced in 802.11a/b/g. Modulation and channel code can be changed on packet-based.
* CP-length and subcarrier mapping can be reconfigured easily.

-----------------

## Download

This software is **free** for non-commercial academic research and education purposes, but registration (free of charge) is required. Please give us an email to register and request for download. We will send you the source code once we receive your request.

Click [here](mailto:jiaxin@ie.cuhk.edu.hk) to contact us.

------------------

## Publications

Our software is basically free. The only requirement is as follow: once you have received our program, you agree to cite our background [paper](https://arxiv.org/abs/2006.09970) below in the event that your work based upon our work results in publications or other research outputs.

<div class="card">
<div class="card-body">
    J. Liang, H. Chen, and S. C. Liew
    Design and Implementation of Time-Sensitive Wireless IoT Networks on Software-Deﬁned Radio
    arXiv:2006.09970 [cs.NI], Jun. 2020
</div>
</div>
