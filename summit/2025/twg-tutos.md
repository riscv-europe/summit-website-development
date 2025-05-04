---
title: TWGs and Tutorials
layout: summit2025
---

{% include jumboboxstart.html
    title = "Tutorials and TWGs/SIGs Meetings"
    lead = "In <b>Louis Armand East-West</b> amphitheaters, and in <b>Rooms 1-3</b>, level S3.<br>*Please note that tutorials are open to the public while TWGs/SIGs require <a href=\"https://riscv.org/members/join/\">RISC-V membership.</a>.*"
%}

Jump to:
 - [Tutorial descriptions](#Tutos).
 - [Details on some of the TWGs, SIGs, and HCs](#TWG-SIG).

{% include jumboboxend.html %}

{% include bannerimg.html
    img = "media/banners/schedule-mon.png"
%}

{% include jumboboxstart.html
    title = "Tutorials"
    lead = "Description of the tutorials"
	id = "Tutos"
%}


### T1.1 -- Intro to RISC-V (aka RISC-V 101)

Come to hear about the What, How and Why of RISC-V!

This tutorial is perfect for anyone curious about RISC-V or looking to
deepen their understanding and engagement. The covered topics are:

 - *What is and Why RISC-V?* by **Keith Graham**, Chair of RISCV
   Academia.
 - *Software & RISC-V* by **Nathan Egge**, winner of the RISC-V Board
   of Directors Software Leadership award.
 - *How to get involved and engage in RISC-V* by **Jeffrey
   Osier-Mixon** and **Flo Wohlrab**.

This tutorial is free and open to the public, but **requires registration**:

<div class="row justify-content-md-center my-4">
    <a href="https://community.riscv.org/events/details/risc-v-international-risc-v-synergy-forums-technical-talks-and-webinars-presents-intro-to-risc-v-summit-europe/" class="btn btn-lg" style="background-color: var(--riscv-y); border-color: var(--riscv-y); width:50%;">Register to <em>Intro to RISC-V (aka RISC-V 101)</em><br> Monday 12 May, 10h00-13h00</a>
</div>


### T1.3 -- RISC-V on FPGA in 90 minutes

**By Dr Per Anderson.**

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


### T2.2 -- XiangShan: An Open-Source High-Performance RISC-V Processor and Infrastructure for Architecture Research

**By Xin Li, Xuan Hu, and Xi Chen.**

This tutorial will present our efforts on the XiangShan project, an
industry-competitive, high performance RISC-V processor
project. Engineers will learn advanced processor design of our
superscalar out-of-order core. Researchers will learn how to use
XiangShan and its agile development infrastructure, MinJie, to make
architecture research more convenient and solid. Open-source
developers will have the opportunity to join us in hands-on
development, and explore typical use cases on XiangShan and MinJie. In
summary, this tutorial aims to provide valuable insights and
experiments for the audience to engage with XiangShan and its
supporting infrastructure, fostering collaboration and innovation in
RISC-V processor development.

**Audience:** researchers and engineers on computer architecture
research, open-source hardware design and agile development
Infrastructure.

**Requirements:** attentees should bring their own laptop. The
presenter will provide access to cloud servers with XiangShan
environment.

**Xin Li** is a CPU design engineer at the Beijing Open-Source Chip
Research Institute. His primary work focuses on open-source hardware
design and CPU modeling. His research interests mainly include memory
subsystems, covering Load-Store Units (LSU), Cache, and Prefetching.

**Xuan Hu** is a PhD candidate student at the University of Chinese
Academy of Sciences, working on CPU architecture and open-source
hardware design. His research interests include out-of-order
schedualing and vector architechture.

**Xi Chen** is a PhD candidate at the University of Chinese Academy of
Sciences, working on CPU architecture and open-source hardware
design. His research interests include memory and cache systems.

### T2.3 -- UnityChip Verification: Open Source Multi-Language Hardware Verification

**By Fangyuan Song and Yunlong Xie.**

This tutorial equips attendees with practical skills to unify hardware
verification across languages and domains. Software engineers will
learn to leverage Python/C++/Java/Golang for hardware validation
without needing deep HDL expertise. Hardware verification engineers
will discover software-driven automation (CI/CD, hybrid
SystemVerilog-Python workflows) to accelerate complex
verification. Open-source developers will gain hands-on experience
with low-cost toolchains (Verilator, Pytest) and collaborative
practices to verify RISC-V or custom chips efficiently. Attendees will
leave with cross-domain strategies, reusable code templates, and
insights to bridge hardware rigor with software agility in modern
verification.

**Audience:** (a) Software Engineers interested in hardware
verification: Leverage Python / C++ skills to validate hardware
without deep HDL expertise. (b) Hardware verification engineers will
discover software-driven automation (CI/CD, hybrid System
Verilog-Python workflows) to accelerate complex verification.
(c)Open-sourcedevelopers will gainh ands-on experience with low-cost
tool chains (Verilator, Pytest) and collaborative practices to verify
RISC-V or custom chips efficiently. Attendees will leave with
cross-domain strategies, reusable code templates, and insights to
bridge hardware rigor with software agility in modern verification.

**Requirements:** A laptop with Linux and pre-installed Docker & VS
Code.

**Fangyuan Song** is a research intern at Beijing Open Source Chip
Research Institute, where he focus on bridging software agility with
hardware reliability in modern verification workflows. His work
centers on developing accessible solutions that empower engineers
across different domains to collaborate effectively on chip
verification – particularly for RISC-V architectures.

**Yunlong Xie** is a PhD candidate at the University of Chinese
Academy of Sciences, working on open-source hardware toolchains for
software-native hardware verification. His research focuses on
enabling more efficient hardware validation through software
methodologies while lowering the verification barrier for software
developers.

### T3.2 -- SC-V MMU Verification of Virtualization and Hypervisor Operation for CPU and SOC Platform

**By Adnan Hamid.**

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


### T3.3 -- The potential of custom instructions, from design to implementation, accelerating the co-design flow

**By Julián Pavón and Iván Vargas.**

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

<p align="center" style="font-size: 0.8em"><a href="#Top" class="backnavigation">To page top</a> &mdash; <a href="#Tutos" class="backnavigation">To tutorials</a></p>

{% include jumboboxend.html %}


{% include jumboboxstart.html
    title = "TWG/SIG Meetings"
    lead = "Description of **Technical Working Groups**, **Special Interest Group**, and **Horizontal Committees** meetings of RISC-V International.<br>*Please note that TWGs/SIGs require <a href=\"https://riscv.org/members/join/\">RISC-V membership.</a>*"
	id = "TWG-SIG"
%}

### Marketing / Event Committee

**Description**

The Marketing & Event Committee serves as a strategic sounding board,
offering feedback, ideas, and guidance on the organization’s marketing
and event initiatives. This is a low-commitment, advisory group meant
to provide diverse perspectives rather than execute tasks.

**Primary functions include**:

 - Offering feedback on event concepts, branding, messaging, and promotional strategies
 - Sharing insights on industry trends, audience engagement, and best practices
 - Brainstorming new ideas for campaigns, content, and community outreach
 - Acting as a test group for reviewing communications or event materials before launch
 - Amplifying initiatives by sharing through personal/professional networks when possible
 - Participation is entirely voluntary and input-driven—members are not expected to take on planning or execution roles.

### CHERI- TG/SIG

**Description of SIG**

The CHERI SIG will work on a strategy for adding Capability Hardware
Enhanced RISC Instructions (CHERI) to the RISC-V ISA. Enabling a
capability-based security model will ensure that RISC-V can provide
strong security guarantees as well as mechanisms for
compartmentalization that are more scalable than traditional
techniques like PMP (physical memory protection) and MMU (memory
management unit). This SIG will work towards defining a CHERI-enabled
instruction set extension, toolchain requirements, programming model
and psABI (processor-specific application binary interface).

**Description of CHERI TG**

Memory safety is the biggest security threat to computer systems:
Microsoft and Google Chromium identifying 70% of their critical
vulnerabilities being in this class. CHERI-based memory safety has
arisen from research starting in 2010 to be the focus of the [Innovate
UK Digital Security by Design Program](https://www.dsbd.tech) (£90m UK
government funding and over £200m from industry). Under this program,
ARM Ltd has produced the Morello prototype: quad-core CHERI-ARM
superscalar processors and GPU on a 7nm TSMC process, demonstrating
little performance or area penalty from adding this security
technology. Initially 1,000 Morello units have been shipped to
partners for evaluation.

Microsoft’s Security Response Center’s 42-page report [Security
Analysis of CHERI
ISA](https://github.com/microsoft/MSRC-Security-Research/blob/master/papers/2020/Security%20analysis%20of%20CHERI%20ISA.pdf)
concludes that over ⅔ of all of Microsoft’s critical memory-safety
vulnerabilities in 2019 would have been deterministically mitigated by
CHERI - the closest competing technology, tagged memory extensions,
achieved only 13% deterministic mitigation. Tens of millions of lines
of C/C++ code have now been ported to CHERI including work by
[Capabilities
Limited](https://www.capabilitieslimited.co.uk/_files/ugd/f4d681_e0f23245dace466297f20a0dbd22d371.pdf)
who measured just 0.026% lines-of-code change when porting an
open-source desktop application stack including X11 and
KDE. Microsoft’s Azure Silicon team has developed and released
[CHERIoT: Rethinking security for low-cost embedded
systems](https://www.capabilitieslimited.co.uk/_files/ugd/f4d681_e0f23245dace466297f20a0dbd22d371.pdf)
that includes an open-source [CHERIoT on
Ibex](https://github.com/microsoft/CherIoT-ibex) - a CHERI extended
embedded RISC-V core that will be taped out in the near future. The
CHERIoT RTOS demonstrates how CHERI can provide scalable
compartmentalisation and memory protection, which is more scalable and
uses comparable silicon area to a PMP (physical memory protection as
defined in the RISC-V privileged spec). The intergovernmental report
[Shifting the Balance of Cybersecurity Risk: Principles and Approaches
for Security-by-Design and
-Default](https://www.cisa.gov/sites/default/files/2023-04/principles_approaches_for_security-by-design-default_508_0.pdf)
recommends CHERI as the secure hardware foundation for future systems,
and also recommends the use of software compartmentalisation that
CHERI supports efficiently.

Given the commercial demonstration of the effectiveness of CHERI,
multiple vendors with in-flight hardware implementationsq, the
practicality of porting software, and the regulatory push toward CHERI
to fundamentally improve

### Security HC

** Mission Description**:

 - Promote RISC-V as a vehicle within the security community
 - Liaise with other internal RISC-V committees and with external security committees
 - Create an information repository on trends, threats and countermeasures
 - Identify top 10 challenges in security for the RISC-V community to address
 - Propose security committees (Marketing or Technical) to tackle specific security topics
 - Recruit security talent to the RISC-V ecosystem (e.g., into committees)
 - Develop consensus around best security practices for all industry technology sectors

### HPC SIG Mission

**Mission**:

Provide a global forum for technical and strategic high pereformance
computing, systems and copmponents (processors, accelerators, etc.)
targeting large scale performance (tera- peta- exa-scale and beyond)
and power targets (any data and compute intensive domain), imperatives
to leverage and enable RISC-V.

### Timing Fences TWG

**Description**:

Covert channels are communication channels that a supervisor cannot
observe or control. Timing channels are covert channels that exploit
timing interferences caused by competition for shared
microarchitectural resources, such as caches, buffers, and branch
predictors. For instance, timing channels can be used to extract
secrets as part of a microarchitectural speculation attack, such as
Spectre-like attacks.

To prevent timing channels, shared hardware resources must be strictly
partitioned between isolated applications. The Timing Fences Task
Group will propose a small ISA extension to enable such partitioning
of shared microarchitectural states. For instance, we will introduce a
temporal fence instruction that can be used to temporally partition
shared on-core microarchitectural states by clearing them, e.g., when
switching between isolated applications.

The proposed RISC-V Timing Fences TG will collaborate to produce:
 - A small ISA extension (possibly no more than one or two instructions, or only a new CSR).
 - A non-normative short guide: defining threat models, developing rationale, etc.
 - A proof-of-concept implementation, including both a prototype RISC-V core and a compiler that manages the necessary intrinsics.
 - A test strategy guide, including a test suite for common covert channels.
 - The Sail model corresponding to this extension.

The TG will work with the appropriate Priv/Unpriv ISA committee,
Architecture Review Committee, and Security HC.

### Soft CPU SIG

**Description**:

The Core-Local Interrupt Controller (CLIC) Privileged Architecture
Extensions are designed to provide low-latency, vectored, pre-emptive
interrupts for RISC-V systems. When activated the CLIC subsumes and
replaces the original RISC-V basic local interrupt scheme. The CLIC
has a base design that requires minimal hardware, but supports
additional extensions to provide hardware acceleration. The goal of
the CLIC is to provide support for a variety of software ABI and
interrupt models, without complex hardware that can impact
high-performance implementations.

### Attached Matrix Ext (AME)

Matrix operations are a key operation in deep-learning training and
inference for workloads like natural-language processing,
recommendation systems, and image recognition. With the pervasive use
of these applications in environments ranging from the datacenter,
through IoT to mobile applications, matrix operations for RISC-V
should scale acrsoss these application domains and apply to
high-performance and resource-constrained environments.

The Matrix Operations Unit TG will specify an attached Matrix
Operations Unit Extension. An attached matrix unit executes
instructions that are part of the processor instruction stream and,
from an architectural perspective, must follow program order. An
attached matrix unit is also self-contained and orthogonal to other
architectural resources: it defines its own set of matrix registers
and uses these as part of its specified operations.

The Matrix Operations Unit will specify an extension to the RISC-V ISA
that implements a scalable (i.e., with the ability to operate on
different operand sizes and allow the writing of matrix-geometry
agnostic code) matrix operations unit. This matrix operations unit
will be a standalone block implementable without dependencies on the
RISC-V Vector extension.

The resulting specification will encompass:
 - an overview of the commonly used matrix operations in established
   algorithms and commonly used software libraries;
 - a specification of the architectural state capable of
   holding/referencing two-dimensional matrix tiles of
   configurable/variable geometry;
 - a specification of those matrix operations supported as part of
   this extension, including at least:
    - load, store, and move operations
       - between memory and the matrix tile architectural state
       - (if implemented together with the RISC-V Vector extension)
         between RISC-V vector registers and rows/columns of the
         matrix tile architectural state
    - matrix-matrix, vector-matrix and scalar-matrix arithmetic
      operations
    - matrix permutation operations
    - sparse-matrix compression/decompression;
 - a predication mechanism to control operations performed on matrix
   tiles;
 - a mapping of matrix operations onto instructions defined in the
   (newly defined) Matrix Operations Extension; and
 - a review of the interactions of matrix load/store and prefetching
   of matrices with the RISC-V memory models and a specification of
   any deviations from the standard RISC-V memory model.

### SoC Infra HC

The SOC infrastructure Horizontal committee contains but is not
limited to the components that straddle the hardware/software boundary
and are necessary to boot and operate systems in every product from
IOT/embedded through Data Center/Cloud and beyond. By their nature
these components are also often matrixed into other committees
pertaining to security, RAS, platforms, etc. The intent is to provide
a robust set of specifications that product implementers need to be
successful while minimizing duplication of effort and fragmentation of
design choices in the RISC-V community.


### Functional Safety SIG

The goal of the Safety SIG (special interest group) within the RISC-V
Foundation is to identify the need for various architectural
principles and hardware interfaces for achieving Functional Safety in
the RISC-V architecture. Focused task groups will be proposed to the
RISC-V Foundation technical committee to be spun off when sufficient
critical mass and discussion depth is reached on a specific topic.

{% include jumboboxend.html %}
