Website Specification Document
==============================

The Website Specification Document (WSD) outlines key objectives and design
decisions relevant to developing the web front-end of the Pitt-Google Broker
(herein *the project* and PGB respectively).

Overview
--------

The current design of the PGB focuses on providing services within a cloud
based environment. While this provides many benefits from a computational and
scalability perspective, familiarity of cloud based services is not common
within all parts of the scientific / astronomical community. To mitigate this
potential obstacle for PGB users, this project is intended to provide a
limited, public web interface for PGB services. This includes (but is not
limited to) providing basic access to PGB data products, either in whole or in
part.

Functionality
-------------

Data Access:
^^^^^^^^^^^^

1. Access to tabulated data for recent alerts / object (e.g. last week or month or 10,000 alerts).
2. Ability for users to define custom topic subscriptions
3. User configurable subscriptions to PGB alert topics
4. User configurable subscriptions notifications. Options to:
   1. Send to email
   2. Subscribe on slack
   3. Alert within website
5. Guides on how to access data in the cloud
6. Options throughout the UI to share data via collaborators, both via email
   and from within the web application.

TOM Integration:
^^^^^^^^^^^^^^^^

1. Management of users' observatory API keys
2. Ability to submit observing requests to remote observatories
3. Alert notifications when observations are completed (email and in site)

Authentication:
^^^^^^^^^^^^^^^

1. Email validation when signing up for a new user account
2. Recaptcha validation when logging in and creating new accounts
3. Ability to authenticate via an existing Google account
4. Permission roles for unauthenticated, general users, staff, and admin

Accessibility
-------------

The project will adhere to WCAG 2.0 guidelines. To assist in this, this
project will use the adherence checklists provided by `wuhcag.com`_.
A minimum of Level 1 accessibility will be provided in final production,
which is formalized below.
These requirements hold across all platforms, including desktop, tablet,
and mobile browsers.
No accessibility requirements are formally imposed during the development
process, only on the final delivered product.


Level 1 Requirements
^^^^^^^^^^^^^^^^^^^^

+------------------------------------------------------------------+-------------------------------------------------------------+
|Guideline                                                         | Summary                                                     |
+==================================================================+=============================================================+
| `1.1.1 – Non-text Content`_                                      | Provide text alternatives for non-text content              |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `1.2.1 – Audio-only and Video-only (Pre-recorded)`_              | Provide an alternative to video-only and audio-only content |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `1.2.2 – Captions (Pre-recorded)`_                               | Provide captions for videos with audio                      |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `1.2.3 – Audio Description or Media Alternative (Pre-recorded)`_ | Video with audio has a second alternative                   |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `1.3.1 – Info and Relationships`_                                | Logical structure                                           |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `1.3.2 – Meaningful Sequence`_                                   | Present content in a meaningful order                       |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `1.3.3 – Sensory Characteristics`_                               | Use more than one sense for instructions                    |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `1.4.1 – Use of Colour`_                                         | Don’t use presentation that relies solely on colour         |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `1.4.2 – Audio Control`_                                         | Don’t play audio automatically                              |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `2.1.1 – Keyboard`_                                              | Accessible by keyboard only                                 |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `2.1.2 – No Keyboard Trap`_                                      | Don’t trap keyboard users                                   |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `2.2.1 – Timing Adjustable`_                                     | Time limits have user controls                              |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `2.2.2 – Pause, Stop, Hide`_                                     | Provide user controls for moving content                    |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `2.3.1 – Three Flashes or Below`_                                | No content flashes more than three times per second         |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `2.4.1 – Bypass Blocks`_                                         | Provide a ‘Skip to Content’ link                            |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `2.4.2 – Page Titled`_                                           | Use helpful and clear page titles                           |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `2.4.3 – Focus Order`_                                           | Logical order                                               |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `2.4.4 – Link Purpose (In Context)`_                             | Every link’s purpose is clear from its context              |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `3.1.1 – Language of Page`_                                      | Page has a language assigned                                |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `3.2.1 – On Focus`_                                              | Elements do not change when they receive focus              |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `3.2.2 – On Input`_                                              | Elements do not change when they receive input              |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `3.3.1 – Error Identification`_                                  | Clearly identify input errors                               |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `3.3.2 – Labels or Instructions`_                                | Label elements and give instructions                        |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `4.1.1 – Parsing`_                                               | No major code errors                                        |
+------------------------------------------------------------------+-------------------------------------------------------------+
| `4.1.2 – Name, Role, Value`_                                     | Build all elements for accessibility                        |
+------------------------------------------------------------------+-------------------------------------------------------------+

.. _wuhcag.com: https://www.wuhcag.com/
.. _1.1.1 – Non-text Content: https://www.wuhcag.com/non-text-content/
.. _1.2.1 – Audio-only and Video-only (Pre-recorded): https://www.wuhcag.com/audio-only-video-only-prerecorded/
.. _1.2.2 – Captions (Pre-recorded): https://www.wuhcag.com/captions-prerecorded/
.. _1.2.3 – Audio Description or Media Alternative (Pre-recorded): https://www.wuhcag.com/audio-description-media-alternative-prerecorded/
.. _1.3.1 – Info and Relationships: https://www.wuhcag.com/info-and-relationships/
.. _1.3.2 – Meaningful Sequence: https://www.wuhcag.com/meaningful-sequence/
.. _1.3.3 – Sensory Characteristics: https://www.wuhcag.com/sensory-characteristics/
.. _1.4.1 – Use of Colour: https://www.wuhcag.com/use-of-colour/
.. _1.4.2 – Audio Control: https://www.wuhcag.com/audio-control/
.. _2.1.1 – Keyboard: https://www.wuhcag.com/keyboard/
.. _2.1.2 – No Keyboard Trap: https://www.wuhcag.com/no-keyboard-trap/
.. _2.2.1 – Timing Adjustable: https://www.wuhcag.com/timing-adjustable/
.. _2.2.2 – Pause, Stop, Hide: https://www.wuhcag.com/pause-stop-hide/
.. _2.3.1 – Three Flashes or Below: https://www.wuhcag.com/three-flashes-or-below/
.. _2.4.1 – Bypass Blocks: https://www.wuhcag.com/bypass-blocks/
.. _2.4.2 – Page Titled: https://www.wuhcag.com/page-titled/
.. _2.4.3 – Focus Order: https://www.wuhcag.com/focus-order/
.. _2.4.4 – Link Purpose (In Context): https://www.wuhcag.com/link-purpose-in-context/
.. _3.1.1 – Language of Page: https://www.wuhcag.com/language-of-page/
.. _3.2.1 – On Focus: https://www.wuhcag.com/on-focus/
.. _3.2.2 – On Input: https://www.wuhcag.com/on-input/
.. _3.3.1 – Error Identification: https://www.wuhcag.com/error-identification/
.. _3.3.2 – Labels or Instructions: https://www.wuhcag.com/labels-or-instructions/
.. _4.1.1 – Parsing: https://www.wuhcag.com/parsing/
.. _4.1.2 – Name, Role, Value: https://www.wuhcag.com/name-role-value/

Hosting
-------

The project will be hosted using the Google Cloud Platform. The web application
itself will be hosted using App Engine while the backend database will rely
on the Cloud SQL service. This choice is motivated by the following factors:

1. PGB Data products are also hosted in the cloud, so deploying to the cloud
   makes it easier to interface the website with PGB data products.
2. Cloud services (App engine and Cloud SQL) scale automatically to meet
   demand. This means we don't have to manage servers or services to meet
   user demand.
3. GCP works on a "pay for what you use" basis. This minimizes operating costs,
   and scales to zero cost during periods of low website traffic.

Project Phases
--------------

This project is broken down into separate development stages listed below.
In general, later phases depend on the completion of work in earlier phases.
However, there is some room for simultaneous work on successive phases.
Late stage phases (5-7) are intentionally left blank, and are to be outlined in
detail before being undertaken.

Phase 1 – Establish a Foundational Website
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This phase is targeted on getting up and running. Focus is placed on getting
most of the heavy lifting out of the for a rudimentary, functional website so
team team members can contribute in later phases during spare or 20% time.

- Design jinja HTML templates for core website pages including:
  - A landing page
  - Getting started pages for describing PGB services and products
  - A page with tabulated data of recently published alerts
  - A page displaying information for a single alert and it's data products
  - A page with tabulated data of recently observed objects
  - A page displaying information for a single object and it's data products

- Build a Django backend capable of supporting the above listed pages. At a minimum include apps for:
  - Interacting ith alert data (`alerts`)
  - Interacting ith object data (`objects`)
  - Signing up new users (`signup`)
  - User profiles (`subscriptions`)

- Add a custom user authentication model to the backend that includes at minimum
  - Username and / or email
  - First and last name
  - Host country / university

- Add forms and pages for adding new users. Tie this to a sign up page

Phase 2 – Documentation and Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This phase is targeted at ensuring the project has a solid foundation for
moving forward efficiently. Some of the work in this phase may have already
been implement in Phase 1 by virtue of good coding habits.

- Use sphinx to write dedicated documentation for
  - Installation instructions
  - Configuring GCP services to support the project
  - Project goals

- Write supplemental documentation for autodoc content generated by sphinx
- Deploy sphinx documentation for the project to Read The Docs
- Configure tests with travis
- Configure style / quality control with code climate or a similar service

Phase 3 – Styling and Content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This phase begins populating the website with static and dynamic content.
This includes technical documentation on PGB services, getting started guides,
PGB data products, etc. Progress at this phase is somewhat limited by the
availability of PGB data products. This phase should be completed to the extent
allowed by the PGB development status, and can be revisited as necessary.

Static content (phase 3a):

- Implement an initial CSS template to style existing HTML templates
- Add CSS styling to the django admin interface
- Add textual content for all existing pages. Much of this can be pulled from
  existing PGB documentation. Place holder text should be avoided when possible.

PGB content (phase 3b):

- Connect the `alerts` app to PGB and populate

Phase 4 – Design review and Deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Validate project meets accessibility requirements
- Acquire external input concerning overall website design and implement
  any desired changes.
- Ensure a minimum of 60% test coverage for the django backend
- Signup pages and contact forms are checked for correct configuration with
  the email backend
- All web pages correctly implement required authentication requirements
- No major error messages rendered by the site
- Functioning website deployed to App Engine with continuous deployment
- Evaluate next steps by outlining phases 5-7

Phase 5 – Adding Content Topic Subscriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Phase 6 – Adding a Collaborative User Platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Phase 7 – Adding TOM Related Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
