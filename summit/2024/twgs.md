---
title: Technical Workgroup Meetings
layout: summit2024
---

{% include bannerimg.html
    img = "media/banners/calista.jpg"
%}

{% include jumboboxstart.html
    title = "Tutorials and Technical Workgroup Meetings"
    lead = "The week of the RISC-V Summit starts with one day of tutorials and technical workgroup meetings."
%}

The technical work groups of RISC-V get the opportunity to meet face-to-face at
this first day of the summit. Those meetings are only open to members.

Additionally there are tutorials that are open to all.

## Monday Program Overview 

<div class="d-flex justify-content-center">
<table class="my-4 table table-sm" style="width: 75%">
  <thead>
    <tr>
      <th>Time</th>
      <th colspan="2" style="text-align: center">Tutorials</th>
      <th colspan="1" style="text-align: center">Hackathon</th>
      <th colspan="2" style="text-align: center">TWG Meetings (Members Only)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Room: TBA</td>
      <td>Room: TBA</td>
      <td>Room: TBA</td> 
      <td>Room: TBA</td>
      <td>Room: TBA</td>
    </tr>
    <tr>
      <td>10:00-11:00</td>
      <td rowspan="2" style="background-color: var(--riscv-sy)">Tutorial:<br> Introduction to RISC-V</td>
      <td>-</td>
      <td>-</td>
      <td style="background-color: var(--riscv-lg)">DTPM SIG</td>
      <td style="background-color: var(--riscv-lg)">Runtime Integrity SIG & Security HC</td>
    </tr>
    <tr>
      <td>11:00-12:00</td>
      <td>-</td>
      <td style="background-color: var(--riscv-lv)">RISC-V Hackathon</td>
      <td style="background-color: var(--riscv-lg)">SoftCPU SIG</td>
      <td>-</td>
    </tr>
    <tr>
      <td>12:00-13:00</td>
      <td colspan="5" style="text-align: center; vertical-align: middle;"> Lunch Break </td>    
    </tr>
     <tr>
      <td>13:00-13:30</td>
      <td rowspan="3" style="background-color: var(--riscv-sy)">Tutorial: X-Heep SoC</td>
      <td>-</td>
      <td rowspan="3" style="background-color: var(--riscv-lv)">RISC-V Hackathon</td>
      <td style="background-color: var(--riscv-lg)">CHERI SIG + TG</td>
      <td style="background-color: var(--riscv-lg)">Technical Starters Guide for RISC-V</td>
    </tr>
     <tr>
      <td>13:30-14:00</td>
      <td>-</td>
      <td style="background-color: var(--riscv-lg)">Fast Interrupt Task Group</td>
      <td style="background-color: var(--riscv-lg)">RISC-V Labs</td>
    </tr>
     <tr>
      <td>14:00-14:30</td>
      <td>-</td>
      <td style="background-color: var(--riscv-lg)">Scalar Efficiency SIG</td>
      <td style="background-color: var(--riscv-lg)">RISC-V Developer Boards Program</td>
    </tr>
     <tr>
      <td>14:30-15:00</td>
     <td colspan="5" style="text-align: center; vertical-align: middle;"> Coffee Break </td>
    </tr>  
    <tr>
      <td>15:00-15:30</td>
      <td rowspan="3" style="background-color: var(--riscv-sy)">Tutorial: LLVM</td>
      <td rowspan="3" style="background-color: var(--riscv-sy)">Tutorial: <br>RISC-V in Education</td>   
      <td rowspan="3" style="background-color: var(--riscv-lv)">RISC-V Hackathon</td>
      <td style="background-color: var(--riscv-lg)">HPC SIG</td>
      <td rowspan="2" style="background-color: var(--riscv-lg)">Marketing Committee</td>
    </tr>
     <tr>
      <td>15:30-16:00</td>    
      <td style="background-color: var(--riscv-lg)">Server Platform TG</td>
    </tr>
    <tr>
      <td>16:00-16:30</td>   
      <td>-</td>
      <td style="background-color: var(--riscv-lg)">RISC-V in Space</td>
    </tr>
     <tr>
      <td>16:30-17:00</td>
      <td colspan="5" style="text-align: center; vertical-align: middle;"> Break</td>
    </tr>
       <tr>
      <td>17:00-18:00</td>
     <td colspan="5" style="text-align: center; vertical-align: middle; background-color: var(--riscv-lg)"> RISC-V International Annual General Meeting (Members Only)</td>
    </tr>
  </tbody>
</table>
</div>

{% include jumboboxend.html %}

{% include jumboboxstart.html
    title = "Technical Workgroup Meetings "
    lead = "Information on technical workgroup meetings. (RISC-V Members only)"
%}

## DTPM SIG

Debug, Trace, and Performance Monitoring Special Interest Group (SIG) coordinates and prioritizes debug, trace and performance monitoring activities for RISC-V.

## Runtime Integrity SIG & Security HC

Runtime Integrity SIG:
Explore and propose security mechanisms related to runtime integrity that may be efficiently implemented at the ISA level, to provide strong security guarantees, and bridge the gap between RISC-V and other architectures.

Security Horizontal Committee:
* Promote RISC-V as an ideal vehicle for the security community
* Liaise with other internal RISC V committees and with external security committees
* Create an information repository on new attack trends, threats and countermeasures
* Identify top 10 open challenges in security for the RISC-V community to address
* Propose security committees (Marketing or Technical) to tackle specific security topics
* Recruit security talent to the RISC-V ecosystem (e.g., into committees)
* Develop consensus around best security practices for IoT devices and embedded systems

More info at https://lists.riscv.org/g/security.

## SoftCPU SIG

The RISC-V Soft-CPU SIG provides a forum to advance RISC-V as the preeminent ecosystem for FPGA processor and SoC designs. The SIG will not deliver any specifications or standards. It will develop overall strategy and establish priorities, then create task groups to develop any identified outputs.

## CHERI SIG + TG

The CHERI SIG will work on a strategy for adding a capability based security model (CHERI) to the RISC-V ISA. Enabling a capability-based security model will ensure that RISC-V can provide strong security guarantees as well as mechanisms for compartmentalization that are more scalable than traditional MMU/PMP-based techniques. This SIG will work towards defining a CHERI-enabled instruction set, toolchain requirements, programming model and psABI.

## Technical Starters Guide for RISC-V

The objective of this presentation is to help technical contributors who are new to RISC-V learn to navigate the information and resources to enable contributions.

## Fast Interrupt Task Group

The aim of the Fast Interrupt Task Group is to: 
* Develop a low-latency, vectored, priority-based, preemptive interrupt scheme for interrupts directed to a single hart, compatible with the existing RISC-V standards
* Provide both hardware specifications and software ABIs/APIs. 
* Standardize compiler conventions for annotating interrupt handler functions.


## RISC-V Labs

RISC-V Labs brings together member companies from across the ecosystem to give developers the resources they need to build and test their software, from porting of existing  projects to development of new components that will power the next wave of computing innovation.

RISC-V Lab Partners provide one or more of the following:

* Continuous Integration (CI) testing of open source software projects
* CI testing resources for use by open source communities to use on their projects
* “Sandbox” instances of RISC-V physical and virtual hardware for open source communities and projects

## Scalar Efficiency SIG

This group works to identify opportunities to improve code size and/or performance by defining new instructions that combined the semantics of existing instructions that commonly occur together.

## RISC-V Developer Boards Program

The RISC-V Developer Boards program serves to evangelize and promote the RISC-V architecture by partnering with RISC-V hardware vendors to donate hardware to projects to:

* Drive success of RISC-V member products and services, to enable operating system distributions support,
* Grow upstream open-source software community adoption, 
* Build educational resources, 
* Embrace emerging technologies which use the RISC-V architecture, and
* Foster software ecosystem engagement and good-will.

Participant projects will submit a plan of usage and be required to document their results using the board. In addition, RISC-V vendor members are running their own programs and coordinating with RISC-V International.

## HPC SIG

Special Interest Group on High-Performance Computing (HPC).
More info at https://lists.riscv.org/g/sig-hpc.

## Marketing Committee

The Marketing Committee seeks to generate awareness and adoption of the RISC-V open collaboration ecosystem and adoption of RISC-V technologies, be an advocate for the organization, and help build the RISC-V brand. They also provide input into the strategic marketing plan, RISC-V marketing activities, and assistance on the execution of marketing efforts. The RISC-V Marketing Committee should be considered by it’s members as an extension of their own marketing department for RISC-V related products, solutions, tools, etc.

## Server Platform TG

The RISC-V Server Platform specification defines a standardized set of hardware and sofware capabilities, that portable system software, such as operating systems and hypervisors, can rely on being present in a RISC-V server platform. 

## RISC-V in Space
Sandi Habinc from Frontgrade Gaisler will discuss applications for RISC-V in space. 


{% include jumboboxend.html %}
