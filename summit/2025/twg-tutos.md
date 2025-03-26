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

**By Julián Pavón and Iván Vargas**

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

**Audience:** The tutorial is tailored for a diverse audience,
encompassing computer architecture researchers with a keen interest in
integrating the RISC-V ISA into their research endeavors, and who seek
a proficient tool to commence their work within this ISA
domain. Moreover, it caters to researchers already immersed in RISC-V,
aiming to augment their design methodology with a comprehensive
top-to-bottom evaluation framework.  Hardware developers exploring
avenues for expedited performance assessment of new RISC-V
instructions, prior to embarking on hardware modules in RTL, will find
substantial value in this tutorial. Additionally, graduate and
undergraduate students with a passion for computer systems and
embedded systems are well-positioned to benefit from this tutorial, as
it provides hands-on coding experiences facilitating the modeling and
evaluation of diverse CPU architectures.

**Requirements:** Have Docker software installed on the laptop used
during the tutorial and download our docker image with all the tools
and libraries dependencies. All the information can be found in the
following page:
<https://sites.google.com/view/tutorial-custom-riscv-instr/home>

**Julián Pavón** *(BSC, UPC) currently a final-year Ph.D. candidate at
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

**Iván Vargas Valdivieso** *(BSC, UPC) is a Ph.D. candidate at the
Universitat Politecnica de Catalunya advised by Dr. Adrian Cristal and
Dr. Osman Unsal.  His research interests are in computer architecture,
Process-in-memory, Vector Architectures, Database Management Systems
and hardware simulators. His research focuses on acceleration of DBMS
through novel hardware-software codesign. Ivan is interested in
hardware innovations in the areas of vector computing, database
management systems and computer architecture simulators. His research
focuses on acceleration of DBMS through novel hardware-software
codesign.*

### RISC-V on FPGA in 90 minutes

**By Dr Per Anderson**

You will see and experience how to replicate the design of a simple
RISC-V processor from scratch to executing programs on an FPGA-board
within the timeframe of this 90-minute tutorial. The take-aways
include how RISC-V can be used to raise educational goals and
accomplishments, as well as the incredible, combined power and
simplicity of open-source tools applied to open architecture
specifications.

**Audience:** The tutorial is directed to anyone interested in how
RISC-V, combined with the power and simplicity of present generation
open-source tools, can be integrated with ease and thereby inspire and
encourage the next, and perhaps present, generation of engineers to
implement RISC-V in their designs.

**Requirements:** Laptops with USB and access to the Internet. FPGA
boards will be provided by lecturers.  One point of the tutorial is to
demonstrate the ease of use emerging from delivering the tools into,
and executing them inside, the user’s web browser without installation
or downloads. Thus, the tutorial can be followed in full using no
other pre-requisites than a (reasonably modern) web browser running on
a laptop.

**Dr Per Anderson** *(Lund Univ.). His main interests are in design of
digital IC:s. He has a background as researcher, lecturer and
entrepreneur and is now responsible for, and currently developing, the
Batchelor level courses in digital design and computer organization at
Lund University. This includes using open-source tools to implement a
RISC-V design on FPGA during the laboratory work of the introductory
course in digital design given in the sophomore year on the EE and CE
programs. The development and dissemination of these activities were
made possible by the EU project CHIPS of Europe and the Swedish Chips
Competence center, SCCC.*

### SC-V MMU Verification of Virtualization and Hypervisor Operation for CPU and SOC Platform

**By Adnan Hamid**

The advent of RISC-V has presented verification teams with many new
verification challenges. Complex interactions at the system level,
that must be considered when developing a RISC-V core, include
uncommon scenarios for block level verification teams. As we move
towards more system-level verification and RISC-V Application
Processors in general, these types of scenarios will become
commonplace. As such, RISC-V verification provides, among many other
things, an interesting learning vehicle for general verification
challenges to come. This workshop will discuss a specific complex, but
yet commonplace, verification challenge for any team working on a
complex RISC-V core. We will consider the verification of a Memory
Management Unit (MMU) that includes virtualization and hypervisor
operation. These scenarios need to consider both Single- and
Multi-core devices along with an Input Output Memory Management Unit
(IOMMU) and uncore IP interaction. The workshop will contain valuable
information for any engineer or manager involved with the design of a
RISC-V core or using a RISC-V core on their SoC.

**Audience:** any engineer involved with the design or verification
of a RISC-V core, or any end user of a core on an SoC.

**Requirements:** None. The tutorial will consist of presentations and
demos, and will not be hands on.

**Adnan Hamid** *is the founder and CTO of Breker and the inventor of
its core technology. Noted as the father of Portable Stimulus, he has
over 20 years of experience in functional verification automation,
much of it spent working in this domain. Prior to Breker, he managed
AMD’s System Logic Division, and also led their verification team to
create the first test case generator providing 100% coverage for an
x86-class microprocessor. In addition, Adnan spent several years at
Cadence Design Systems and served as the subject matter expert in
system-level verification, developing solutions for Texas Instruments,
Siemens/Infineon, Motorola/Freescale, and General Motors. Adnan holds
twelve patents in test case generation and synthesis. He received BS
degrees in Electrical Engineering and Computer Science from Princeton
University, and an MBA from the University of Texas at Austin.*

{% include jumboboxend.html %}
