# QA Test Matrix

Run tests at unit, API integration, mobile integration, end-to-end,
security, and operational levels. Every release must include regression
of booking/payment/entry/exit.

## 1. Authentication and roles

  -----------------------------------------------------------------------
  ID                Scenario          Expected result   Priority
  ----------------- ----------------- ----------------- -----------------
  AUTH-01           Valid OTP         Session           P0
                                      established       

  AUTH-02           Expired/reused    Rejected          P0
                    OTP                                 

  AUTH-03           Repeated OTP      Rate-limited      P0
                    requests                            

  AUTH-04           Driver calls      403/denied        P0
                    admin endpoint                      

  AUTH-05           Attendant         Denied            P0
                    accesses another                    
                    facility                            

  AUTH-06           Suspended         Denied and        P0
                    operator attempts audited           
                    mutation                            
  -----------------------------------------------------------------------

## 2. Vehicle and facility compatibility

  -----------------------------------------------------------------------
  ID                Scenario          Expected result   Priority
  ----------------- ----------------- ----------------- -----------------
  VEH-01            Create each       Saved with        P0
                    supported vehicle correct category  
                    category                            

  VEH-02            Truck searches    Excluded/not      P0
                    car-only facility bookable          

  VEH-03            Vehicle exceeds   Rejected with     P0
                    height/weight     clear reason      
                    limit                               

  VEH-04            Facility disables New bookings      P0
                    a category        blocked           

  FAC-01            Unverified        Not publicly      P0
                    facility search   bookable          

  FAC-02            Entrance pin      Directions use    P1
                    differs from      entrance pin      
                    property centroid                   

  FAC-03            Facility hours    Correct           P1
                    cross midnight    local-time        
                                      behavior          
  -----------------------------------------------------------------------

## 3. Search and availability

  --------------------------------------------------------------------------
  ID                Scenario             Expected result   Priority
  ----------------- -------------------- ----------------- -----------------
  SRCH-01           Search by GPS        Nearby eligible   P0
                                         results           

  SRCH-02           Location denied      Manual search     P1
                                         works             

  SRCH-03           Stale capacity feed  UI labels         P0
                                         stale/unknown; no 
                                         false live claim  

  SRCH-04           No matching facility Useful empty      P1
                                         state             

  SRCH-05           Invalid              Validation error  P1
                    coordinates/radius                     

  SRCH-06           Search large radius  Bounded response  P1
                                         and pagination    
  --------------------------------------------------------------------------

## 4. Booking concurrency and state

  -------------------------------------------------------------------------
  ID                Scenario            Expected result   Priority
  ----------------- ------------------- ----------------- -----------------
  BOOK-01           One available unit, At most one       P0
                    two concurrent      hold/booking      
                    requests            succeeds          

  BOOK-02           Duplicate request   Same logical      P0
                    with same           result, no        
                    idempotency key     duplicate booking 

  BOOK-03           Expired quote       Rejected;         P0
                                        re-quote required 

  BOOK-04           Hold expires        Capacity released P0
                                        exactly once      

  BOOK-05           Operator blocks     Transaction       P0
                    capacity during     prevents oversell 
                    booking                               

  BOOK-06           Walk-in consumes    Online booking    P0
                    last unit           rejected          

  BOOK-07           Cancel confirmed    Policy applied    P0
                    booking             and capacity      
                                        handled correctly 

  BOOK-08           Timezone/daylight   Correct local     P1
                    or midnight         schedule and UTC  
                    boundary            storage           

  BOOK-09           Booking extension   Rejected or       P0
                    overlaps another    alternative       
                    reservation         offered           
  -------------------------------------------------------------------------

## 5. Payments and refunds

  -------------------------------------------------------------------------
  ID                Scenario          Expected result     Priority
  ----------------- ----------------- ------------------- -----------------
  PAY-01            Successful        Booking/payment     P0
                    payment webhook   transition validly  

  PAY-02            Client claims     Not confirmed as    P0
                    success but       paid                
                    provider says                         
                    failed                                

  PAY-03            Invalid webhook   Rejected and logged P0
                    signature         safely              

  PAY-04            Duplicate webhook No duplicate state  P0
                                      transition/refund   

  PAY-05            Webhooks arrive   State remains       P0
                    out of order      consistent after    
                                      reconciliation      

  PAY-06            Payment pending   Clear pending       P0
                    timeout           state;              
                                      reconciliation path 

  PAY-07            Refund provider   Retry/reconcile     P0
                    timeout           idempotently        

  PAY-08            Partial refund    Correct balance and P1
                                      receipt             

  PAY-09            Price changes     New price disclosed P0
                    after quote       and reaccepted      
                    expiry                                
  -------------------------------------------------------------------------

## 6. QR, entry, exit, sessions

  -------------------------------------------------------------------------
  ID                Scenario            Expected result   Priority
  ----------------- ------------------- ----------------- -----------------
  QR-01             Valid credential at Validated         P0
                    correct                               
                    facility/time                         

  QR-02             Forged or random    Rejected          P0
                    token                                 

  QR-03             Credential at wrong Rejected          P0
                    facility                              

  QR-04             Cancelled/expired   Rejected          P0
                    booking                               

  QR-05             Replay after entry  Rejected or       P0
                                        handled per       
                                        explicit policy   

  SES-01            Duplicate entry     One entry event   P0
                    tap/request                           

  SES-02            Exit without entry  Rejected or       P0
                                        audited exception 
                                        flow              

  SES-03            Overstay            Correct disclosed P0
                                        policy applied    

  SES-04            Walk-in entry and   Same capacity     P0
                    exit                ledger and        
                                        receipt flow      

  SES-05            Network down at     No false          P0
                    attendant scanner   validation; clear 
                                        recovery path     
  -------------------------------------------------------------------------

## 7. Operator/admin

  -----------------------------------------------------------------------
  ID                Scenario          Expected result   Priority
  ----------------- ----------------- ----------------- -----------------
  OPS-01            Operator edits    New quote uses    P0
                    price             correct effective 
                                      rule              

  OPS-02            Capacity adjusted Actor, reason,    P0
                                      and timestamp     
                                      audited           

  OPS-03            Operator uploads  Rejected safely   P1
                    invalid document                    

  OPS-04            Admin approves    State transition  P0
                    facility          and audit event   

  OPS-05            Unauthorized      Denied and        P0
                    refund            audited           

  OPS-06            Facility          Defined handling  P0
                    suspended with    and notifications 
                    active bookings                     
  -----------------------------------------------------------------------

## 8. Flutter UX and resilience

  -----------------------------------------------------------------------------------
  ID                Scenario                      Expected result   Priority
  ----------------- ----------------------------- ----------------- -----------------
  UX-01             App resumes during payment    Fetch             P0
                                                  authoritative     
                                                  booking/payment   
                                                  state             

  UX-02             Slow network/double tap       Progress shown;   P0
                                                  server            
                                                  idempotency       
                                                  protects          

  UX-03             Empty/loading/error/offline   Clear next action P1
                    states                                          

  UX-04             Large text/screen reader      Critical flows    P1
                                                  usable            

  UX-05             Location permission denied    Manual            P1
                                                  destination path  
                                                  works             

  UX-06             App killed during booking     State recoverable P0
                                                  from server       

  UX-07             Notification permission       Booking remains   P1
                    denied                        visible in app    
  -----------------------------------------------------------------------------------

## 9. Non-functional checks

-   Load: search under representative concurrent traffic; set targets
    after baseline.
-   Latency: track p50/p95/p99 by endpoint and provider.
-   Reliability: simulate database and Redis failures; booking state
    must remain correct.
-   Security: OWASP-aligned API tests, authorization matrix, dependency
    scan, secret scan.
-   Privacy: logs and analytics contain no raw tokens, OTPs, card data,
    or unnecessary plate/phone values.
-   Backup: restore a production-like backup to an isolated environment.
-   Accessibility: text scaling, contrast, screen-reader labels, focus
    order.
-   Mobile: supported iOS/Android versions, low-memory devices,
    permission variations.
-   Release: smoke test install, login, search, quote, booking, payment
    sandbox, QR, cancellation/refund.

## 10. P0 release gate

No release if any P0 test fails. Any waived P0 requires written risk
acceptance from the product owner and a documented mitigation; payment
correctness, access control, and double-booking prevention should not be
waived for public launch.
