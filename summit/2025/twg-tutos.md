---
title: TWGs and Tutorials
layout: summit2025
---

{% include bannerimg.html
    img = "media/banners/tutorials.jpg"
%}

{% include jumboboxstart.html
    title = "Tutorials and Technical Working Group Meetings"
    lead = "Get updated and up to speed on RISC-V before the core Summit!"
%}



{% include jumboboxend.html %}

{% include jumboboxstart.html
    title = "Tutorials"
    lead = "Description of the tutorials<br>(Tutorials rooms and schedule TBD)"
%}

### The potential of custom instructions, from design to implementation, accelerating the co-design flow

Our objective is to enhance the efficiency of designing and evaluating
new instructions within the RISC-V ISA, thereby reducing the entry
barriers for researchers seeking to apply RISC-V to their respective
domain-specific challenges. We will provide a comprehensive
explanation about our top-to-bottom evaluation framework, which
enables quick design and evaluation of new RISC-V instructions going
through software stack integration to performance simulation.

The instructional program will comprise a blend of informative
lectures and interactive lab sessions. Initially, participants will
receive a comprehensive overview of diverse tools essential for both
software and hardware development tailored to platforms supporting the
RISC-V ISA. Subsequently, we will delve into the specifics of our
evaluation framework, elucidating the utilization of one ISA emulator
(QEMU) alongside a computer architecture simulator (gem5).

Furthermore, we will elucidate the integration methodology of these
tools to expedite software development of new instructions via ISA
emulators and to assess the performance of the developed instructions
using computer architecture simulators. To facilitate hands-on
learning, we will furnish our evaluation framework through a docker
image, encompassing the aforementioned tools, along with requisite
wrappers and scripts for seamless integration.

Additionally, practical exercises and example code will be provided
during the lab sessions, enabling attendees to gain firsthand
experience in the design, integration, and evaluation of new RISC-V
instructions using our framework. Ultimately, all participants will
depart equipped with the evaluation framework, code samples, and the
necessary proficiency to employ them as foundational elements in their
individual research endeavor.

*Requirements:* Have Docker software installed on the laptop used
during the tutorial and download our docker image with all the tools
and libraries dependencies. All the information can be found in the
following page:
<https://sites.google.com/view/tutorial-custom-riscv-instr/home>

**Julian Pavon** *(BSC, UPC) currently a final-year Ph.D. candidate at
the Universitat Politecnica de Catalunya advised by Dr. Adrian Cristal
and Dr.  Osman Unsal. His research interests are centered around
Computer Architecture, Vector Architectures, and RTL design. Julian's
primary focus involves the design of innovative Vector Processing
Units capable of accelerating applications with irregular memory
access patterns across various domains, including sparse algebra,
databases, and genome sequence analysis.  His contributions have been
published in different top-tier venues. Julian has worked designing
and developing different hardware modules for multiple RISC-V cores
manufactured.*

**Ivan Vargas Valdivieso** *(BSC, UPC) is a Ph.D. candidate at the
Universitat Politecnica de Catalunya advised by Dr. Adrian Cristal and
Dr. Osman Unsal.  His research interests are in computer architecture,
Process-in-memory, Vector Architectures, Database Management Systems
and hardware simulators. His research focuses on acceleration of DBMS
through novel hardware-software codesign. Ivan is interested in
hardware innovations in the areas of vector computing, database
management systems and computer architecture simulators. His research
focuses on acceleration of DBMS through novel hardware-software
codesign.*

{% include jumboboxend.html %}
