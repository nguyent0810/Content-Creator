# VIDEO CREATION SYSTEM SPECIFICATION
Phiên bản: 1.0 — Contract chính thức của Video Creation Pipeline.

Tài liệu này là **specification**, không phải audit, không phải blueprint, không phải mô tả code hiện có. Nó độc lập với implementation, độc lập với model, độc lập với prompt cụ thể, độc lập với domain. Mọi implementation tương lai (Python, Node, LLM-orchestrated, hybrid, hay bất kỳ công nghệ nào khác) **phải tuân theo tài liệu này**. Nếu một implementation mâu thuẫn với specification, implementation đó được coi là sai — không phải specification sai.

Từ khoá bắt buộc dùng trong toàn tài liệu: **phải** (MUST — bắt buộc tuyệt đối, không có ngoại lệ), **không được phép** (MUST NOT — cấm tuyệt đối), **nên** (SHOULD — khuyến nghị mạnh, có thể có ngoại lệ có ghi chú), **có thể** (MAY — tuỳ chọn).

---

## 1. Core Principles

### P1 — Narration là Source of Truth duy nhất
**Định nghĩa:** Toàn bộ nội dung ngữ nghĩa (ý nghĩa, thực thể, hành động, cảm xúc, quan hệ nhân quả) của mọi output thị giác phải bắt nguồn từ, và chỉ từ, văn bản narration đã được duyệt. Không có nguồn nào khác (kiến thức nền của model, quy ước thể loại, thư viện mẫu, trí nhớ của lượt sinh trước) được phép là nguồn gốc của nội dung ngữ nghĩa.

**Rationale:** Nếu có hơn một nguồn sự thật, hệ thống không thể xác định output nào là "đúng" khi có mâu thuẫn, và không có cách nào kiểm chứng độc lập nội dung sinh ra khớp với ý định biên tập ban đầu.

**Consequence nếu vi phạm:** Output trôi dần khỏi kịch bản gốc mà không ai phát hiện được — vì mọi phép so khớp chỉ có ý nghĩa khi có đúng một nguồn để so khớp.

### P2 — Visual chỉ được suy diễn trong phạm vi Narration
**Định nghĩa:** Mọi chủ thể, hành động, bối cảnh, vật thể xuất hiện trong output thị giác phải là (a) trích dẫn trực tiếp, (b) diễn giải có thể truy vết 1-1, hoặc (c) suy luận biểu tượng được đánh dấu tường minh là suy luận (không phải trích dẫn) từ narration. Không nội dung thị giác nào được phép tồn tại mà không có một trong ba loại liên hệ trên.

**Rationale:** Ranh giới giữa "diễn giải hợp lý" và "bịa đặt" chỉ có thể giữ vững nếu có một quy tắc rõ ràng, áp dụng như nhau cho mọi trường hợp, thay vì để lại cho phán đoán tự do của từng lượt sinh.

**Consequence nếu vi phạm:** Đạo cụ/bối cảnh không có căn cứ xuất hiện lặp lại như một tập filler quen thuộc, làm loãng và đôi khi mâu thuẫn với nội dung thật của kịch bản.

### P3 — Generator không được tự chứng nhận kết quả
**Định nghĩa:** Tác nhân (người, model, script) tạo ra nội dung thị giác không được phép là tác nhân duy nhất xác nhận nội dung đó đạt yêu cầu chất lượng. Mọi khẳng định "đạt yêu cầu" phải đến từ một tầng khác, với input/quy trình tách biệt.

**Rationale:** Một tác nhân đánh giá chính sản phẩm của mình, bằng chính lý lẽ đã dùng để tạo ra sản phẩm đó, về mặt logic không thể phát hiện ra sai sót xuất phát từ chính lý lẽ đó.

**Consequence nếu vi phạm:** Chỉ số chất lượng luôn có xu hướng hội tụ về "đạt", bất kể chất lượng thực tế — hệ thống mất khả năng tự phát hiện suy thoái.

### P4 — Mọi output phải truy vết được về nguồn
**Định nghĩa:** Với bất kỳ đơn vị output cuối cùng nào, phải tồn tại một chuỗi liên kết tường minh, không đứt đoạn, dẫn ngược về đúng đoạn narration đã sinh ra nó (xem Mục 4).

**Rationale:** Truy vết được là điều kiện cần để kiểm chứng được — không truy vết được đồng nghĩa với không kiểm chứng được, bất kể output trông hợp lý đến đâu.

**Consequence nếu vi phạm:** Không ai (kể cả chính hệ thống) có thể phân biệt output đúng nhưng diễn đạt khéo với output sai nhưng diễn đạt khéo.

### P5 — Quyết định ngữ nghĩa phải đi trước quyết định trình bày
**Định nghĩa:** "Cái gì phải xuất hiện" (chủ thể, hành động, bối cảnh, ý nghĩa) phải được quyết định và cố định trước khi "trình bày như thế nào" (câu chữ, khung hình, ống kính) được quyết định. Không được phép đảo ngược thứ tự này.

**Rationale:** Nếu trình bày được quyết định trước hoặc đồng thời với ngữ nghĩa, hệ thống có xu hướng dùng trình bày (đổi từ ngữ, đổi góc máy) để tạo cảm giác đa dạng thay vì tạo đa dạng ngữ nghĩa thật.

**Consequence nếu vi phạm:** "Fake uniqueness" — output khác nhau ở bề mặt câu chữ nhưng giống nhau ở nội dung thị giác thực chất.

### P6 — Tính duy nhất (uniqueness) được định nghĩa bởi Scene Identity, không bởi hình thức chuỗi ký tự
**Định nghĩa:** Hai output được coi là "giống nhau" hay "khác nhau" dựa trên Scene Fingerprint (Mục 6), không dựa trên việc chuỗi ký tự/văn bản của chúng có trùng nhau hay không.

**Rationale:** Chuỗi ký tự gần như luôn luôn có thể làm cho khác nhau bằng cách đổi từ ngữ, ngay cả khi nội dung thị giác giống hệt nhau — nên phép đo dựa trên chuỗi ký tự không có khả năng phát hiện lặp về bản chất.

**Consequence nếu vi phạm:** Chỉ số "0 repetition" trở thành đúng-về-mặt-toán-học nhưng vô nghĩa-về-mặt-nội-dung.

### P7 — Continuity là trạng thái được quản lý tường minh, không phải hiệu ứng phụ ngẫu nhiên
**Định nghĩa:** Sự nhất quán của nhân vật, vật thể, bối cảnh, mốc thời gian xuyên suốt toàn bộ sản phẩm phải được theo dõi bởi một cơ chế trạng thái tường minh (Continuity State), không được phép chỉ là kết quả tình cờ của việc mỗi đơn vị output "nhớ" lại đơn vị trước đó theo trí nhớ tự do.

**Rationale:** Trí nhớ tự do không có ranh giới rõ ràng về việc gì được phép mang sang, gì không — dẫn tới cả hai lỗi đối nghịch: rò rỉ continuity không mong muốn và mất continuity mong muốn.

**Consequence nếu vi phạm:** Vật thể/nhân vật xuất hiện sai bối cảnh, hoặc biến mất không lý do, mà không ai xác định được ranh giới trách nhiệm.

### P8 — Domain và chủ đề là ngoại vi (external), không phải một phần contract lõi
**Định nghĩa:** Kiến thức domain (giáo lý Phật giáo, quy tắc y khoa, quy ước tài chính...) được nạp như một lớp ràng buộc phụ trợ (domain safety/representation policy), không được nhúng cứng vào bất kỳ stage nào của pipeline lõi.

**Rationale:** Pipeline lõi phải hoạt động giống hệt nhau về cấu trúc bất kể domain — chỉ nội dung ràng buộc phụ trợ thay đổi.

**Consequence nếu vi phạm:** Pipeline phải viết lại cho mỗi domain mới, và không có cách nào đảm bảo hai domain khác nhau tuân theo cùng một mức độ nghiêm ngặt.

---

## 2. Canonical Pipeline Specification

```
Narration
   ↓
Semantic Extraction
   ↓
Semantic Beat
   ↓
Visual Obligation
   ↓
Shot Planning
   ↓
Continuity Planning
   ↓
Scene Planning
   ↓
Prompt Composition
   ↓
Independent QA
   ↓
Final Prompt
```

Pipeline này là **tuyến tính về phụ thuộc dữ liệu** (mỗi stage chỉ tiêu thụ output của (các) stage trước nó và trạng thái tích luỹ do Continuity Planning quản lý) nhưng **không bắt buộc tuyến tính về công nghệ thực thi** — specification không quy định stage nào do người, model, hay script thực hiện.

### 2.1 Narration
- **Purpose:** Là điểm neo sự thật duy nhất cho toàn bộ pipeline (P1).
- **Input:** Văn bản narration đã được duyệt ở cấp biên tập, ở dạng plain text hoàn chỉnh.
- **Output:** Chính nó — không biến đổi. Narration không bị pipeline này sửa đổi dưới bất kỳ hình thức nào.
- **Owner:** Ngoài phạm vi pipeline (thuộc quy trình biên tập nội dung, xảy ra trước pipeline này).
- **Invariant:** Bất biến trong suốt vòng đời của một lần chạy pipeline. Nếu narration thay đổi, mọi output phía sau phải được coi là stale và chạy lại.
- **Forbidden behaviors:** Pipeline không được phép sửa, rút gọn, diễn giải lại, hay bổ sung nội dung vào narration ở bất kỳ điểm nào.
- **Acceptance criteria:** Narration tồn tại, là văn bản hoàn chỉnh, không rỗng.

### 2.2 Semantic Extraction
- **Purpose:** Trích xuất các đơn vị sự thật ngôn ngữ có thể tham chiếu lại được (thực thể, hành động, quan hệ) từ narration, làm nguyên liệu thô cho việc phân đoạn.
- **Input:** Toàn văn Narration.
- **Output:** Tập thực thể (entities), hành động (actions), quan hệ (relations) — mỗi phần tử neo vào một vị trí cụ thể trong narration (span).
- **Owner:** Semantic Extraction sở hữu "cái gì có thật trong văn bản". Không stage nào phía sau được phép bổ sung thực thể mới không có trong output của stage này.
- **Invariant:** Mọi phần tử output phải neo được vào một span cụ thể, không rỗng, của narration.
- **Forbidden behaviors:** Không được suy diễn thực thể/hành động không xuất hiện dưới dạng chuỗi con hoặc từ đồng nghĩa trực tiếp trong narration. Không được tổng quát hoá một thực thể cụ thể thành một danh mục trừu tượng (ví dụ: biến "chiếc ghế" thành "một biểu tượng của sự vắng mặt" ở chính stage này — tổng quát hoá, nếu cần, chỉ được phép xảy ra tường minh ở các stage sau, có đánh dấu).
- **Acceptance criteria:** Mỗi thực thể/hành động/quan hệ trích xuất có span hợp lệ; hợp toàn bộ span phải phủ narration mà không làm mất nghĩa nào không được ghi nhận.

### 2.3 Semantic Beat
- **Purpose:** Nhóm các đơn vị sự thật thành các đơn vị ý nghĩa (beat) — ranh giới ngữ nghĩa nhỏ nhất mà pipeline coi là "một ý hoàn chỉnh".
- **Input:** Output của Semantic Extraction.
- **Output:** Danh sách Semantic Beat theo Mục 3.1.
- **Owner:** Sở hữu "ranh giới ý nghĩa" — là đơn vị không được các stage sau chia nhỏ hơn về mặt NGỮ NGHĨA (dù có thể chia nhỏ hơn về số lượng đơn vị render ở Shot Planning).
- **Invariant:** Tập hợp `source_span` của toàn bộ beat phải phủ 100% narration, không chồng lấn nhau.
- **Forbidden behaviors:** Không được tạo beat không có `source_span`. Không được gộp hai ý không liên quan nhân quả/chủ đề vào một beat chỉ để thuận tiện.
- **Acceptance criteria:** 100% narration được phủ bởi đúng một beat cho mỗi vị trí văn bản; mỗi beat có `meaning` diễn giải được đối chiếu ngược lại `evidence`.

### 2.4 Visual Obligation
- **Purpose:** Xác định "cái gì bắt buộc phải được nhìn thấy" để truyền tải một Semantic Beat, tách biệt hoàn toàn khỏi việc "nhìn thấy như thế nào".
- **Input:** Một Semantic Beat.
- **Output:** Một hoặc nhiều Visual Obligation theo Mục 3.2.
- **Owner:** Sở hữu "nghĩa vụ nội dung". Không sở hữu và không được quyết định camera, khung hình, ánh sáng.
- **Invariant:** Mỗi Visual Obligation phải trích được `evidence` không rỗng từ đúng Semantic Beat cha của nó.
- **Forbidden behaviors:** Không được là một "scene" (đã có bối cảnh/hành động cụ thể hoá hoàn chỉnh); không được là một "prompt" (đã có câu chữ trình bày); không được là một "template" (không được sao chép từ một khuôn có sẵn không gắn với beat cụ thể).
- **Acceptance criteria:** `required_subject`/`required_action` của mọi Visual Obligation phải truy vết được về `evidence`; số lượng Visual Obligation của một beat phải phản ánh đúng độ phức tạp ngữ nghĩa của beat đó, không phải một con số cố định áp đặt từ ngoài.

### 2.5 Shot Planning
- **Purpose:** Quyết định cách trình bày cinematic (bao nhiêu đơn vị hình ảnh, vai trò từng đơn vị, ý đồ dàn cảnh) cho một Semantic Beat, dựa trên toàn bộ Visual Obligation của beat đó — quyết định trước khi cụ thể hoá từng đơn vị riêng lẻ.
- **Input:** Một Semantic Beat + toàn bộ Visual Obligation thuộc beat đó.
- **Output:** Shot Plan theo Mục 3.3 — tập shot, mỗi shot map tới ít nhất một Visual Obligation.
- **Owner:** Sở hữu "kịch bản dựng cảnh cấp beat". Không sở hữu việc chọn vật thể cụ thể (đó là Scene Planning) và không sở hữu continuity xuyên-beat (đó là Continuity Planning).
- **Invariant:** Mọi Visual Obligation của beat phải được đại diện bởi ít nhất một shot; không shot nào được tồn tại mà không đại diện cho ít nhất một Visual Obligation.
- **Forbidden behaviors:** Không được tạo shot chỉ để đạt một số lượng clip mục tiêu (ví dụ: chia nhỏ một beat thành nhiều shot hơn mức ngữ nghĩa yêu cầu, chỉ để lấp đầy thời lượng).
- **Acceptance criteria:** `required_visual_evidence` của Shot Plan phủ đúng 100% Visual Obligation của beat, không thiếu không thừa.

### 2.6 Continuity Planning
- **Purpose:** Quản lý trạng thái xuyên suốt toàn bộ sản phẩm (không chỉ trong một beat) — nhân vật, vật thể, bối cảnh, mốc thời gian, và các hành động chưa khép lại.
- **Input:** Continuity State hiện tại (tích luỹ từ mọi beat trước) + Shot Plan của beat hiện tại.
- **Output:** Continuity State cập nhật (Mục 3.4) + xác nhận/từ chối các `continuity_dependency` mà Shot Plan khai báo.
- **Owner:** Là tầng **duy nhất** được phép biết "điều gì đã xảy ra trước đó". Không stage nào khác được phép tự tham chiếu ngược về các beat/shot trước mà không đi qua tầng này.
- **Invariant:** Một entity (nhân vật/vật thể/bối cảnh) chỉ được tham chiếu là "đã tồn tại" nếu trạng thái vòng đời của nó (Mục 7) đang ở `active` hoặc `referenced`.
- **Forbidden behaviors:** Không được cho phép một entity được dùng ở trạng thái `resolved` mà không có `re-introduced` tường minh; không được bỏ qua việc cập nhật trạng thái sau mỗi beat.
- **Acceptance criteria:** Mọi `continuity_dependency` do Shot Planning khai báo phải được Continuity Planning xác nhận hoặc từ chối tường minh — không được bỏ qua.

### 2.7 Scene Planning
- **Purpose:** Cụ thể hoá từng shot thành nội dung thị giác cụ thể (chủ thể chính xác, vật thể phụ, bối cảnh cụ thể) — dựa trên Shot Plan và Continuity State, có kiểm tra tần suất/nguồn gốc.
- **Input:** Shot Plan (từ 2.5) + Continuity State hiện hành (từ 2.6).
- **Output:** Nội dung cụ thể hoá cho mỗi shot — chủ thể, vật thể, bối cảnh — mỗi phần tử gắn nhãn nguồn gốc (trích từ evidence / motif đã duyệt / suy luận biểu tượng có lý do).
- **Owner:** Sở hữu "lựa chọn cụ thể" — là ranh giới duy nhất nơi một Visual Obligation trừu tượng được ánh xạ xuống một vật thể/hình ảnh cụ thể.
- **Invariant:** Mọi vật thể cụ thể được chọn phải thuộc đúng một trong ba loại: (a) truy vết được về `evidence` của Visual Obligation; (b) là motif toàn cục đã được duyệt tường minh (không tự phát sinh); (c) đánh dấu là suy luận biểu tượng (`ABSTRACT_METAPHOR` hoặc tương đương) kèm lý do bằng văn bản.
- **Forbidden behaviors:** Không được chọn vật thể chỉ vì nó đã được dùng ở shot trước ("quen tay") mà không thuộc một trong ba loại trên; không được vượt ngưỡng tần suất toàn cục cho một Scene Fingerprint mà không có `causal_dependency` giải thích rõ đây là callback có chủ đích.
- **Acceptance criteria:** 100% vật thể xuất hiện trong output của stage này có nhãn nguồn gốc hợp lệ; không entity nào vi phạm cap tần suất toàn cục mà không có giải trình.

### 2.8 Prompt Composition
- **Purpose:** Chuyển đổi (render) nội dung đã được quyết định đầy đủ ở các stage trước thành văn bản/định dạng cuối cùng dành cho công cụ sinh video.
- **Input:** Output của Scene Planning cho một shot + ràng buộc trình bày toàn cục (phong cách hình ảnh, ràng buộc an toàn domain).
- **Output:** Prompt hoàn chỉnh, sẵn sàng gửi cho công cụ tạo video bên ngoài.
- **Owner:** Sở hữu duy nhất "cách diễn đạt bằng ngôn ngữ trình bày". Xem Mục 8 để biết đầy đủ ràng buộc.
- **Invariant:** Không một thực thể ngữ nghĩa mới nào (chủ thể, vật thể, quan hệ) được phép xuất hiện lần đầu tại stage này.
- **Forbidden behaviors:** Xem Mục 8.
- **Acceptance criteria:** Mọi danh từ/động từ chỉ nội dung xuất hiện trong Prompt phải truy vết được ngược về Scene Planning; câu văn hợp lệ về ngữ pháp/cấu trúc theo Mục 10.

### 2.9 Independent QA
- **Purpose:** Đánh giá khách quan, độc lập chất lượng của Final Prompt (và mọi stage trung gian dẫn tới nó) trước khi được coi là output chính thức.
- **Input:** Toàn bộ chuỗi trace từ Narration đến Final Prompt của TOÀN BỘ sản phẩm (không phải một phần/một batch).
- **Output:** QA Result theo Mục 3.6.
- **Owner:** Sở hữu "phán quyết khách quan cuối cùng". Xem Mục 9 để biết đầy đủ ràng buộc độc lập.
- **Invariant:** QA không được là cùng tác nhân, cùng phiên thực thi, hay có quyền truy cập nội bộ vào lý lẽ mà các stage 2.1–2.8 đã dùng.
- **Forbidden behaviors:** Xem Mục 9 và Mục 11.
- **Acceptance criteria:** Xem Mục 10.

### 2.10 Final Prompt
- **Purpose:** Là output chính thức, sẵn sàng bàn giao cho công cụ tạo video bên ngoài.
- **Input:** Prompt Composition output đã được Independent QA xác nhận PASS.
- **Output:** Chính nó — điểm cuối của pipeline.
- **Owner:** Không thuộc sở hữu của bất kỳ stage tạo nội dung nào — chỉ tồn tại sau khi Independent QA xác nhận.
- **Invariant:** Không tồn tại "Final Prompt" nào chưa qua Independent QA với kết quả PASS.
- **Forbidden behaviors:** Không được đánh dấu là "final" nếu QA Result có `overall_status: FAIL` hoặc chưa chạy.
- **Acceptance criteria:** Có một QA Result hợp lệ, `computed_by: INDEPENDENT_PASS`, `overall_status: PASS` gắn kèm.

---

## 3. Canonical Data Model

### 3.1 Semantic Beat

| Field | Bắt buộc | Ràng buộc |
|---|---|---|
| `source_span` | **Bắt buộc** | Vị trí chính xác trong narration gốc; không rỗng; không chồng lấn beat khác |
| `meaning` | Bắt buộc | Diễn giải súc tích; phải đối chiếu được với `evidence` |
| `entities` | Bắt buộc | Mỗi phần tử truy vết được về `source_span` |
| `actions` | Bắt buộc | Mỗi phần tử truy vết được về `source_span` |
| `causal_relation` | Bắt buộc (có thể rỗng nếu beat là điểm khởi đầu độc lập, nhưng phải tường minh ghi nhận "không có") | Nếu có, phải trỏ tới beat khác đã tồn tại, đứng trước theo thứ tự narration |
| `emotional_context` | Bắt buộc | Không được chỉ tồn tại ngầm định trong văn bản trình bày ở stage sau — phải là dữ liệu của chính beat |
| `evidence` | **Bắt buộc** | Trích dẫn/paraphrase-traceable trực tiếp từ `source_span` |

**Ràng buộc chốt:** Không được phép tồn tại một Semantic Beat mà `source_span` rỗng hoặc không trỏ được về narration thật. Một beat không có evidence không phải là một beat hợp lệ — nó không được đi tiếp vào pipeline.

### 3.2 Visual Obligation

| Field | Bắt buộc | Ràng buộc |
|---|---|---|
| `required_subject` | **Bắt buộc** | Truy vết được về `evidence` của beat cha, hoặc đánh dấu tường minh là suy luận biểu tượng |
| `required_action` | Bắt buộc | Không được là giá trị rỗng hoặc không mang nghĩa hành động |
| `required_setting` | Bắt buộc | Nhất quán với Continuity State đang active |
| `optional_cinematic_freedom` | Không bắt buộc | Phạm vi được phép biến thiên tự do ở Shot Planning/Prompt Composition (ví dụ: góc máy, không ảnh hưởng ngữ nghĩa) — phải khai báo tường minh biên độ tự do, không mặc định "mọi thứ đều tự do" |
| `forbidden_hallucination` | Khuyến nghị | Danh sách vật thể bị cấm dùng cho obligation này dù phổ biến ở nơi khác |
| `evidence` | **Bắt buộc, không rỗng** | Chuỗi con hoặc paraphrase-traceable của `evidence` cấp beat |

**Ràng buộc chốt:** Visual Obligation không phải Scene (chưa có bối cảnh cụ thể hoá); không phải Prompt (chưa có câu chữ trình bày); không phải Template (không được rút ra từ một khuôn có sẵn không gắn với `evidence` của chính nó).

### 3.3 Shot Plan

| Field | Bắt buộc | Ràng buộc |
|---|---|---|
| `purpose` | **Bắt buộc** | Mục đích tường thuật của shot này, không phải mô tả hình ảnh |
| `evidence_represented` | **Bắt buộc** | Danh sách `Visual Obligation` mà shot này đại diện — không rỗng |
| `narrative_function` | Bắt buộc | Vai trò trong mạch kể (ví dụ: thiết lập, chuyển tiếp, khai triển chi tiết, callback...) |
| `continuity_dependency` | Bắt buộc (có thể là danh sách rỗng nếu shot không phụ thuộc gì) | Mỗi phụ thuộc phải được Continuity Planning xác nhận trước khi shot được coi là hợp lệ |
| `composition_intent` | Bắt buộc | Ý đồ dàn cảnh ở mức khái niệm (ví dụ: "làm nổi bật sự cô lập") — không phải chỉ đạo camera cụ thể (đó là phạm vi `optional_cinematic_freedom` của Visual Obligation) |

**Ràng buộc chốt:** Không được tồn tại shot chỉ để tăng số lượng clip. Một shot chỉ hợp lệ nếu `evidence_represented` không rỗng.

### 3.4 Continuity State

| Field | Bắt buộc | Ràng buộc |
|---|---|---|
| `characters` | **Bắt buộc** | Danh sách nhân vật đang được theo dõi, kèm trạng thái vòng đời (Mục 7) |
| `objects` | **Bắt buộc** | Tương tự, cho vật thể — bao gồm cả tần suất sử dụng toàn cục (phục vụ Mục 6) |
| `locations` | **Bắt buộc** | Bối cảnh đang active, kèm thuộc tính bị khoá (ánh sáng, thời gian trong ngày, kiến trúc...) |
| `timeline` | **Bắt buộc** | Mốc thời gian tích luỹ, đảm bảo không có mốc thời gian không khả thi (Mục 7) |
| `unresolved_actions` | Bắt buộc | Hành động đã được `introduced` nhưng chưa `resolved` — dùng để phát hiện continuity bị bỏ dở |
| `dependencies` | Bắt buộc | Tập hợp mọi `continuity_dependency` đã được xác nhận, cùng shot/beat đã khai báo chúng |

**Ràng buộc chốt:** Không cho phép một `object`/`character` xuất hiện trong bất kỳ Scene Planning nào nếu nó chưa từng được `introduced` trong Continuity State.

### 3.5 Prompt

**Định nghĩa chốt:** Prompt **chỉ là rendering**. Nó không phải nơi quyết định nội dung. Mọi quyết định ngữ nghĩa (Semantic Beat, Visual Obligation, Shot Plan, Scene Planning) phải hoàn tất **trước khi** Prompt được soạn.

| Field | Bắt buộc | Ràng buộc |
|---|---|---|
| `rendered_text` | **Bắt buộc** | Văn bản cuối cùng — mọi danh từ/động từ chỉ nội dung trong đây phải truy vết được về Scene Planning |
| `source_shot_id` | **Bắt buộc** | Liên kết ngược 1-1 tới Shot Plan đã sinh ra nó |
| `presentation_only_elements` | Không bắt buộc | Các yếu tố thuần trình bày được phép tự do biến thiên (cách diễn đạt câu, thứ tự mô tả) — phải phân biệt tường minh với các yếu tố mang nội dung |

### 3.6 QA Result

**Định nghĩa chốt:** QA Result không chỉ là PASS/FAIL — nó phải là một hồ sơ đầy đủ, tự giải trình được.

| Field | Bắt buộc | Ràng buộc |
|---|---|---|
| `semantic_alignment` | **Bắt buộc** | Kết quả đối chiếu Visual Obligation với Prompt thực tế — không được là bản sao của dữ liệu do stage sinh nội dung tự khai |
| `continuity_alignment` | **Bắt buộc** | Kết quả đối chiếu `continuity_dependency` với Continuity State thực tế |
| `hallucination` | **Bắt buộc** | Danh sách đầy đủ (không chỉ số đếm) mọi thực thể không truy vết được |
| `repetition` | **Bắt buộc** | Tính theo Scene Fingerprint (Mục 6), không theo chuỗi ký tự |
| `grammar` | **Bắt buộc** | Danh sách lỗi cấu trúc/ngữ pháp, nếu có |
| `evidence_trace` | **Bắt buộc** | Với mỗi số liệu ở trên, dẫn ngược lại đúng dữ liệu thô đã dùng để tính ra nó |
| `confidence` | **Bắt buộc** | Mức tin cậy của chính phép đánh giá này (không phải của nội dung được đánh giá) — vì một số phép kiểm (ví dụ: đánh giá biên độ suy luận biểu tượng) có thể có phần chủ quan |
| `failure_reason` | Bắt buộc nếu `overall_status = FAIL` | Giải thích cụ thể, không chỉ mã lỗi |

**Ràng buộc chốt:** QA Result không được phép chỉ chứa `PASS`/`FAIL` mà không có các trường chi tiết ở trên đi kèm. Một QA Result không có `evidence_trace` là một QA Result không hợp lệ.

---

## 4. Traceability Contract

Mọi Final Prompt bắt buộc truy ngược được theo đúng chuỗi:

```
Prompt
   ↓
Shot
   ↓
Visual Obligation
   ↓
Semantic Beat
   ↓
Narration Span
```

**Quy tắc:**
- Mỗi mũi tên trong chuỗi trên là một liên kết bắt buộc, tường minh, có thể kiểm tra lại được (không phải suy luận "chắc là từ đó mà ra").
- Nếu **mất trace ở bất kỳ bước nào** trong chuỗi (ví dụ: một Prompt không dẫn ngược được về đúng một Shot, hoặc một Shot không dẫn ngược được về ít nhất một Visual Obligation), **output đó không hợp lệ** — bất kể nội dung trông hợp lý, đúng ngữ pháp, hay đúng phong cách hình ảnh đến đâu.
- Tính hợp lệ về traceability là điều kiện **tiên quyết**, tách biệt khỏi và đứng trước mọi đánh giá chất lượng khác (semantic alignment, continuity, grammar...). Một output mất trace không được đưa vào đánh giá chất lượng — nó bị loại ngay ở bước kiểm tra traceability.
- Traceability phải đúng theo hướng ngược (Prompt → Narration) **và** hướng xuôi (Narration → Prompt) phải nhất quán: nếu đi xuôi từ một Narration Span, phải tìm lại được ít nhất một Prompt tương ứng (trừ phần narration được xử lý bởi cùng một Semantic Beat với phần khác đã có Prompt — không được có Narration Span "im lặng" không sinh ra bất kỳ output nào mà không có lý do tường minh).

---

## 5. Information Preservation Rules

| Loại thông tin | Bắt buộc giữ | Được phép suy diễn | Không bao giờ được tự phát minh |
|---|---|---|---|
| **Ý nghĩa (`meaning`)** | ✔ Phải giữ nguyên ý định của narration | Diễn giải súc tích hơn, miễn giữ đúng ý | Đổi ý nghĩa gốc thành một ý nghĩa khác dù "gần giống" |
| **Quan hệ nhân quả (`causal_relation`)** | ✔ Phải giữ nguyên thứ tự và hướng nhân-quả | Làm tường minh một quan hệ ngầm định rõ ràng trong văn bản | Thêm một quan hệ nhân quả không có căn cứ, hoặc đảo ngược nhân-quả để "gọn" hơn |
| **Danh tính thực thể (`entity identity`)** | ✔ Một thực thể cụ thể (một người, một vật, một nơi chốn cụ thể) phải giữ đúng danh tính xuyên suốt | Đổi cách gọi tên (đồng nghĩa, đại từ) miễn không đổi danh tính | Gộp hai thực thể khác nhau thành một, hoặc tách một thực thể thành hai |
| **Cảm xúc (`emotional_context`)** | ✔ Phải phản ánh đúng cường độ và loại cảm xúc mà narration truyền tải | Diễn đạt lại bằng từ vựng thị giác khác nhưng cùng loại/cường độ | Thay thế bằng một cảm xúc chung chung không đặc thù cho beat đó |

**Quy tắc cấm tường minh (ví dụ bắt buộc phải tránh):**

Không được phép thay:
```
meaning
causal_relation
entity_identity
```
thành:
```
generic_mood
generic_symbolism
generic_scene
```

Nói cách khác: khi một stage không chắc chắn về cách thể hiện cụ thể, nó **không được phép hạ cấp thông tin cụ thể xuống một phạm trù chung chung** để "cho an toàn". Nếu không đủ căn cứ để thể hiện cụ thể, quy trình đúng là đánh dấu tường minh "suy luận biểu tượng, lý do X" (theo `optional_cinematic_freedom`/visual-mode biểu tượng đã định nghĩa ở Mục 2.4, 2.7) — không phải âm thầm thay thế bằng một khái niệm mơ hồ hơn rồi trình bày như thể nó tương đương với nội dung gốc.

---

## 6. Scene Identity Specification

### 6.1 Scene Concept

**Định nghĩa chính thức:** Một Scene được xác định danh tính (identity) bởi đúng bốn thành phần:

```
subject           — chủ thể chính, đã chuẩn hoá đồng nghĩa
   +
action            — hành động chính, đã chuẩn hoá theo nhóm ngữ nghĩa
   +
setting           — bối cảnh, đã chuẩn hoá
   +
narrative_purpose — vai trò của scene này trong mạch kể (thiết lập / chuyển tiếp /
                     khai triển / callback / kết...)
```

**Một Scene KHÔNG được xác định danh tính bởi:**
```
camera
lens
lighting
weather
wording
adjectives
```

Các yếu tố này là thuộc tính trình bày (presentation attributes) — chúng có thể biến thiên tự do (và **nên** biến thiên để tránh đơn điệu về mặt điện ảnh) mà không làm thay đổi danh tính của scene. Ngược lại, hai scene có camera/lighting/wording khác nhau hoàn toàn nhưng cùng subject+action+setting+narrative_purpose **vẫn được coi là cùng một Scene Concept**.

### 6.2 Scene Fingerprint

**Định nghĩa chính thức:** Scene Fingerprint là biểu diễn chuẩn hoá của Scene Concept, dùng làm khoá so sánh cho mọi mục đích liên quan đến tính duy nhất/lặp lại.

**Contract của Scene Fingerprint:**
1. **Bất biến với hình thức diễn đạt (wording-invariant):** hai biểu đạt ngôn ngữ khác nhau cho cùng một subject phải cho ra cùng một Scene Fingerprint.
2. **Bất biến với trình bày điện ảnh (presentation-invariant):** thay đổi camera/lighting/weather không được làm thay đổi Scene Fingerprint.
3. **Nhạy với thay đổi danh tính (identity-sensitive):** thay đổi thật sự ở subject, action, setting, hoặc narrative_purpose **phải** làm thay đổi Scene Fingerprint.
4. **Toàn cục, không cục bộ (global, not local):** Scene Fingerprint phải được so sánh trên **toàn bộ sản phẩm**, không chỉ giữa các đơn vị liền kề hay trong cùng một lô xử lý — vì lặp lại có thể xảy ra ở hai vị trí cách xa nhau.
5. **Có bộ nhớ tích luỹ (cumulative memory):** hệ thống phải duy trì một sổ tần suất Scene Fingerprint xuyên suốt toàn sản phẩm (Episode Memory), không phải tính lại từ đầu mỗi lần so sánh cục bộ.
6. **Phân biệt được lặp-có-chủ-đích với lặp-ngẫu-nhiên:** một Scene Fingerprint được phép lặp lại nếu có `causal_dependency`/callback tường minh trong Continuity State giải thích lý do; nếu không có giải thích, lặp lại vượt ngưỡng đã định phải bị từ chối.

**Ràng buộc cấm tuyệt đối:** Scene Fingerprint **không được phép** được tính bằng: hash của văn bản đã render, so khớp chuỗi ký tự, hay bất kỳ hình thức nào phụ thuộc vào cách diễn đạt cụ thể của Prompt.

---

## 7. Continuity Contract

Mỗi entity (Character, Object, Location, Action) phải trải qua đúng vòng đời sau, không được bỏ qua bước nào:

```
introduced
   ↓
active
   ↓
referenced
   ↓
resolved
```

**Định nghĩa từng trạng thái:**
- **`introduced`** — entity xuất hiện lần đầu, được Continuity Planning ghi nhận với đầy đủ thuộc tính định danh.
- **`active`** — entity đang trong phạm vi ảnh hưởng trực tiếp của scene/beat hiện tại.
- **`referenced`** — entity không còn active trực tiếp nhưng vẫn được nhắc lại/ngụ ý (ví dụ: một nhân vật đã rời khung hình nhưng câu chuyện vẫn nói về họ).
- **`resolved`** — entity không còn cần thiết cho phần còn lại của sản phẩm (câu chuyện đã khép lại vai trò của nó), hoặc bị thay thế tường minh bởi một `re-introduction` mới.

**Quy tắc bắt buộc:**
- Một entity chỉ được dùng trong Scene Planning nếu trạng thái hiện tại của nó là `introduced`, `active`, hoặc `referenced`. Dùng một entity ở trạng thái chưa từng `introduced`, hoặc đã `resolved` mà không có `re-introduced` tường minh, là vi phạm.
- Mọi entity `introduced` phải có một con đường hợp lệ tiến tới `resolved` (hoặc được duy trì `active`/`referenced` cho tới hết sản phẩm một cách có chủ đích) — không được để lại ở trạng thái lấp lửng không rõ ràng.

**Không cho phép — ba anti-pattern continuity:**

| Anti-pattern | Định nghĩa | Vì sao bị cấm |
|---|---|---|
| **Spontaneous appearance** | Entity xuất hiện trong output mà không có bước `introduced` trước đó | Vi phạm P7 — continuity không còn là trạng thái quản lý được, mà là ngẫu nhiên |
| **Unexplained disappearance** | Entity ở trạng thái `active` biến mất khỏi output tiếp theo mà không chuyển qua `referenced`/`resolved` | Người xem/QA không thể phân biệt đây là lỗi hay chủ đích |
| **Impossible timeline** | Hai trạng thái của cùng một entity/location mâu thuẫn về thời gian (ví dụ: một bối cảnh vừa được đánh dấu "đêm" vừa "giữa trưa" trong cùng một continuity window không có chuyển cảnh) | Phá vỡ tính nhất quán mà Continuity State tồn tại để bảo đảm |

---

## 8. Prompt Composition Contract

**Prompt Composer chỉ được phép:**
```
chuyển Shot (đã được Scene Planning cụ thể hoá đầy đủ) thành Prompt (văn bản trình bày)
```

**Prompt Composer không được phép:**

| Hành vi bị cấm | Vì sao |
|---|---|
| **Tạo semantic mới** | Mọi nội dung ngữ nghĩa phải đã được quyết định ở Visual Obligation/Scene Planning (P5) — Prompt Composition chỉ render, không quyết định |
| **Tạo continuity mới** | Continuity chỉ được quản lý bởi Continuity Planning (P7) — Prompt Composer không có quyền truy cập để "tự nhớ" hay "tự suy diễn" liên kết với các shot khác |
| **Thêm symbolism** | Ý nghĩa biểu tượng (nếu có) phải đã được xác lập và gắn nhãn tường minh ở Scene Planning — không được ứng biến thêm ở bước render cuối |
| **Thêm props không có evidence** | Đây chính là điểm mà hallucination xảy ra nếu không bị chặn — mọi vật thể phải đã qua kiểm tra nguồn gốc ở Scene Planning trước khi tới đây |
| **Sửa narrative** | Prompt Composer không có thẩm quyền diễn giải lại ý đồ tường thuật — đó là thẩm quyền của Semantic Beat/Shot Planning |

**Hệ quả của contract này:** nếu một Final Prompt chứa nội dung không truy vết được về Scene Planning, lỗi đó **thuộc trách nhiệm của Prompt Composer** (vi phạm ranh giới ở Mục 8), không thuộc trách nhiệm của các stage trước — bất kể nguyên nhân gốc sâu xa hơn (ví dụ: Scene Planning không cung cấp đủ chi tiết) có thể truy ngược ở tầng khác.

---

## 9. Independent QA Specification

### 9.1 Yêu cầu độc lập

Generator (mọi stage từ 2.1 đến 2.8) và QA (2.9) **phải độc lập** theo cả ba chiều:
- **Độc lập về tác nhân:** không được là cùng một tác nhân thực thi.
- **Độc lập về phiên làm việc:** không được chạy trong cùng một phiên/lượt suy luận đã tạo ra nội dung được đánh giá.
- **Độc lập về căn cứ:** không được dựa vào bất kỳ khẳng định nào do generator tự đưa ra về chất lượng của chính nó.

### 9.2 QA không được đọc

- **Internal reasoning của generator** — lý lẽ nội bộ mà các stage sinh nội dung đã dùng để tự thuyết phục một lựa chọn là hợp lý.
- **Self-reported coverage** — bất kỳ trường dữ liệu nào do generator tự khai là "đã bao phủ đủ", "đã kiểm tra", "đạt yêu cầu".
- **Self-generated checklist** — danh sách tiêu chí do chính generator tạo ra để tự áp dụng cho mình.

### 9.3 QA chỉ được đánh giá từ

- **Narration** (nguồn gốc, để đối chiếu ngược).
- **Semantic Beat** (để kiểm continuity/traceability của tầng ngữ nghĩa).
- **Shot** (để kiểm continuity/coverage của tầng dàn cảnh).
- **Final Prompt** (đối tượng cuối cùng cần đánh giá).

Bốn nguồn này là **quan sát được, khách quan** — không phải diễn giải hay khẳng định của generator về chính bốn nguồn đó.

### 9.4 QA phải định nghĩa rõ (không được để mặc định/ngầm hiểu)

| Khái niệm | Định nghĩa bắt buộc |
|---|---|
| **Semantic mismatch** | Có ít nhất một `required_subject`/`required_action` của Visual Obligation không được thể hiện, hoặc bị thể hiện sai lệch, trong Final Prompt tương ứng — xác định bằng đối chiếu trực tiếp nội dung Prompt với `evidence`, không bằng cách sao chép nhãn "đã bao phủ" có sẵn |
| **Hallucination** | Có ít nhất một thực thể trong Final Prompt không thuộc bất kỳ loại nào trong ba loại nguồn gốc hợp lệ đã định nghĩa ở Mục 2.7 (truy vết evidence / motif đã duyệt / suy luận biểu tượng có lý do) |
| **Repetition** | Hai hoặc nhiều Scene có cùng Scene Fingerprint (Mục 6) mà không có `causal_dependency` tường minh giải thích, vượt ngưỡng tần suất đã định — đánh giá trên toàn sản phẩm, không theo lô cục bộ |
| **Continuity failure** | Vi phạm bất kỳ quy tắc nào ở Mục 7 (spontaneous appearance / unexplained disappearance / impossible timeline), hoặc một `continuity_dependency` được khai báo nhưng không được Continuity Planning xác nhận |
| **Grammar failure** | Prompt chứa cấu trúc câu không hợp lệ, thiếu thành phần ngữ pháp bắt buộc, hoặc chứa mảnh dữ liệu rò rỉ từ các trường cấu trúc nội bộ (không phải văn bản trình bày có chủ đích) |
| **Evidence failure** | Bất kỳ liên kết nào trong chuỗi Traceability Contract (Mục 4) bị đứt |

---

## 10. Acceptance Criteria

### 10.1 Semantic Alignment PASS khi:
- Subject đầy đủ — mọi `required_subject` của Visual Obligation liên quan được thể hiện trong Final Prompt.
- Action đầy đủ — tương tự, cho `required_action`.
- Causal relation giữ nguyên — quan hệ nhân-quả giữa các Semantic Beat liên quan không bị đảo/mất khi thể hiện thành chuỗi Shot/Prompt.
- Không phát minh sự kiện — không có hành động/sự kiện nào trong Final Prompt mà không truy vết được về `evidence`.

### 10.2 Visual Uniqueness PASS khi:
- **Scene Fingerprint khác nhau** giữa các Scene được so sánh.
- **Không tính** các yếu tố sau vào việc đánh giá "khác nhau": camera; lighting; framing; color grading; wording. Hai Scene chỉ khác nhau ở các yếu tố này **vẫn được coi là cùng một Scene Fingerprint**, và do đó vẫn phải chịu kiểm tra `repetition` theo Mục 9.4 nếu vượt ngưỡng tần suất.

### 10.3 Continuity Alignment PASS khi:
- Mọi entity xuất hiện đều ở trạng thái vòng đời hợp lệ (Mục 7) tại thời điểm xuất hiện.
- Mọi `continuity_dependency` được khai báo ở Shot Plan có xác nhận tương ứng từ Continuity Planning.
- Không có vi phạm spontaneous appearance / unexplained disappearance / impossible timeline.

### 10.4 Traceability PASS khi:
- Chuỗi Prompt → Shot → Visual Obligation → Semantic Beat → Narration Span nguyên vẹn, không đứt đoạn, cho 100% Final Prompt.

### 10.5 Overall PASS khi và chỉ khi:
- **Tất cả** các mục 10.1–10.4 đều PASS, **và** Grammar/Hallucination/Repetition (Mục 9.4) đều không phát hiện vi phạm vượt ngưỡng đã định, **và** QA Result có `computed_by: INDEPENDENT_PASS`.
- Không tồn tại khái niệm "PASS một phần" ở cấp sản phẩm cuối cùng — một Final Prompt hoặc đạt toàn bộ tiêu chí, hoặc không được coi là Final Prompt.

---

## 11. Forbidden Behaviors

| Anti-pattern | Định nghĩa | Vì sao bị cấm |
|---|---|---|
| **Generic filler** | Chèn nội dung mô tả không mang thông tin ngữ nghĩa cụ thể (ví dụ: một khung câu cố định lặp lại chỉ để lấp đầy độ dài) | Vi phạm P2/P5 — nội dung không bắt nguồn từ narration, chỉ tồn tại để trình bày đủ độ dài |
| **Template cycling** | Luân phiên qua một tập nhỏ các khuôn mẫu có sẵn (câu, cấu trúc, bố cục) một cách hệ thống | Vi phạm P6 — tạo cảm giác đa dạng bằng cách xoay vòng hình thức, không phải đa dạng nội dung thật |
| **Scene pool fallback** | Khi không đủ căn cứ, tự động chọn một vật thể/bối cảnh từ một tập "quen thuộc" đã dùng trước đó thay vì báo thiếu căn cứ | Vi phạm P2 — biến việc thiếu thông tin thành một quyết định ngầm định thay vì một tín hiệu cần xử lý tường minh (đánh dấu suy luận biểu tượng có lý do, theo Mục 2.7) |
| **Modulo selection** | Chọn phương án theo chu kỳ toán học (ví dụ: phương án thứ N mod K) thay vì theo căn cứ ngữ nghĩa | Vi phạm P1/P2 — lựa chọn không còn xuất phát từ nguồn sự thật, mà từ một quy tắc số học vô nghĩa với nội dung |
| **Hash-based uniqueness** | Dùng hash/checksum của văn bản đã render làm tiêu chí xác định "duy nhất" | Vi phạm P6 — về bản chất toán học, gần như luôn cho kết quả duy nhất bất kể nội dung có lặp hay không, nên không có khả năng phát hiện lặp thật |
| **Wording uniqueness** | Coi việc thay đổi từ ngữ/cách diễn đạt là đủ điều kiện để tính là "khác nhau" | Vi phạm P6 — đây là hình thức cụ thể của fake uniqueness (P5), tách biệt hình thức khỏi nội dung |
| **Hallucinated props** | Vật thể/chi tiết xuất hiện trong output mà không truy vết được về narration | Vi phạm P2/P4 — phá vỡ điều kiện truy vết được, làm output không thể kiểm chứng |
| **Fake continuity** | Tạo cảm giác nhất quán (dùng lại tên gọi, dùng lại motif) mà không thực sự đi qua Continuity State — ví dụ: hai lần dùng "cùng một vật thể" nhưng thực chất không được Continuity Planning xác nhận là cùng một entity | Vi phạm P7 — continuity trở thành hiệu ứng bề mặt thay vì trạng thái được quản lý thật |
| **Self-certification QA** | QA do generator tự thực hiện, tự khai kết quả | Vi phạm P3 — về logic không thể phát hiện sai sót xuất phát từ chính lý lẽ đã tạo ra sai sót đó |
| **Coverage-copy tautology** | Trường "đã bao phủ" được gán bằng cách sao chép trực tiếp từ trường "cần bao phủ", không qua đối chiếu độc lập với nội dung thực tế | Vi phạm P3/Mục 9.4 — tạo ra chỉ số luôn luôn đúng theo cấu trúc dữ liệu, không phản ánh nội dung thật |
| **Batch-blind QA** | Đánh giá lặp lại/nhất quán chỉ trong phạm vi một lô nhỏ, không trên toàn sản phẩm | Vi phạm Mục 6.2 (yêu cầu "toàn cục, không cục bộ") — bỏ lọt lặp lại xảy ra ở hai vị trí cách xa nhau |
| **Undocumented pipeline vocabulary** | Các khái niệm/trường dữ liệu cốt lõi (tên stage, tên field) không được định nghĩa trong bất kỳ tài liệu spec chính thức nào, chỉ tồn tại ngầm định trong một lần thực thi cụ thể | Vi phạm P1/P4 ở cấp hệ thống — không có gì để đối chiếu lại giữa hai lần chạy, hai người review, hay hai implementation khác nhau |

---

## 12. System Invariants

Các invariant sau **phải đúng với mọi episode và mọi domain**, không có ngoại lệ theo nội dung hay theo quy mô sản phẩm:

1. **Narration luôn là source of truth.** (P1) — không có ngoại lệ "trường hợp đặc biệt được phép bịa".
2. **Semantic không được sinh sau Shot.** Thứ tự bắt buộc là Semantic Beat → Visual Obligation → Shot Planning, không được đảo ngược hay sinh song song không đồng bộ (P5).
3. **Prompt không được quyết định nội dung.** Prompt Composition là rendering thuần tuý (Mục 3.5, Mục 8).
4. **QA phải độc lập.** Không có ngoại lệ "vì tiết kiệm chi phí" hay "vì episode ngắn" (P3, Mục 9).
5. **Mọi output phải traceable.** Không có khái niệm "output hợp lệ nhưng không cần truy vết được" (P4, Mục 4).
6. **Continuity là trạng thái quản lý, không phải trí nhớ tự do.** (P7, Mục 7).
7. **Tính duy nhất được đo bằng Scene Fingerprint, không bằng hình thức.** (P6, Mục 6).
8. **Mọi metric công bố phải neo được vào `evidence_trace`.** Không có chỉ số nào được chấp nhận ở dạng "khẳng định trần trụi" không kèm căn cứ tính toán lại được (Mục 3.6).
9. **Domain logic là ngoại vi, pipeline lõi không đổi theo domain.** (P8, Mục 13).
10. **Không có trạng thái "Final" nào tồn tại trước khi Independent QA PASS.** (Mục 2.10, Mục 10.5).

---

## 13. Domain Independence

Specification này **không hard-code cho bất kỳ episode hay domain cụ thể nào**. Pipeline lõi (Mục 2), Data Model (Mục 3), Traceability Contract (Mục 4), Scene Identity (Mục 6), Continuity Contract (Mục 7), và Independent QA (Mục 9) áp dụng **giống hệt về cấu trúc** cho mọi domain, bao gồm nhưng không giới hạn ở:

- **Buddhism / tôn giáo:** ràng buộc phụ trợ domain (ví dụ: quy tắc thể hiện tôn kính, tránh diễn giải sai giáo lý) được nạp như một tập `forbidden_hallucination`/ràng buộc trình bày bổ sung ở Mục 3.2 và Mục 8 — không thay đổi cấu trúc pipeline.
- **History (Lịch sử):** `evidence` ở Mục 3.1/3.2 ánh xạ tới nguồn sử liệu; ràng buộc "không suy diễn ngoài phạm vi ghi chép" là một biểu hiện cụ thể của P2.
- **Documentary:** `narrative_purpose` (Mục 6.1) ánh xạ trực tiếp tới cấu trúc hồi/chương của phim tài liệu.
- **Education (Giáo dục):** `Visual Obligation` ánh xạ tới mục tiêu học tập cụ thể của từng đoạn nội dung; `evidence` ánh xạ tới giáo trình nguồn.
- **Medical (Y khoa):** ràng buộc phụ trợ nghiêm ngặt hơn ở Mục 3.2 (`forbidden_hallucination`) để tránh thể hiện sai thông tin lâm sàng — nhưng cơ chế kiểm (Mục 9) không đổi.
- **Finance (Tài chính):** tương tự, ràng buộc phụ trợ về tránh cam kết/khẳng định kết quả tài chính là một lớp bổ sung, không phải thay đổi pipeline lõi.
- **Storytelling (hư cấu nói chung):** `entities`/`causal_relation` (Mục 3.1) ánh xạ tới nhân vật/cốt truyện hư cấu; "narration" ở Mục 2.1 vẫn là kịch bản/văn bản nguồn đã duyệt, dù nội dung là hư cấu chứ không phải sự kiện có thật — nguyên tắc P1 vẫn giữ nguyên: mọi visual vẫn phải bắt nguồn từ chính văn bản kịch bản, không tự sáng tác thêm.

**Quy tắc kiểm tra domain-independence cho mọi implementation:** nếu một quy tắc trong tài liệu vận hành nội bộ chỉ áp dụng được cho một domain cụ thể và không thể phát biểu lại dưới dạng tổng quát (ví dụ: một quy tắc chỉ có nghĩa với "Đức Phật" mà không thể khái quát thành "nhân vật có ràng buộc thể hiện đặc biệt"), quy tắc đó **không thuộc phạm vi pipeline lõi** — nó phải được đặt ở lớp ràng buộc phụ trợ domain, tham chiếu vào Mục 3.2/Mục 8, không được sửa cấu trúc Mục 2–12.

---

## 14. Compliance Checklist

Checklist này là **tiêu chuẩn nghiệm thu chính thức**. Mọi implementation tương lai phải tự đánh giá từng dòng là `PASS`, `FAIL`, hoặc `NOT APPLICABLE` (kèm lý do nếu chọn NOT APPLICABLE).

### 14.1 Core Principles (Mục 1)

| # | Invariant | PASS | FAIL | N/A |
|---|---|---|---|---|
| 1.1 | Narration là source of truth duy nhất cho mọi nội dung ngữ nghĩa | ☐ | ☐ | ☐ |
| 1.2 | Mọi nội dung thị giác suy diễn trong phạm vi narration, có đánh dấu loại liên hệ (trích dẫn/diễn giải/suy luận biểu tượng) | ☐ | ☐ | ☐ |
| 1.3 | Generator không tự chứng nhận kết quả của chính nó | ☐ | ☐ | ☐ |
| 1.4 | Mọi output truy vết được về nguồn | ☐ | ☐ | ☐ |
| 1.5 | Quyết định ngữ nghĩa đi trước quyết định trình bày | ☐ | ☐ | ☐ |
| 1.6 | Tính duy nhất được định nghĩa bởi Scene Identity, không bởi chuỗi ký tự | ☐ | ☐ | ☐ |
| 1.7 | Continuity là trạng thái quản lý tường minh | ☐ | ☐ | ☐ |
| 1.8 | Domain logic tách biệt khỏi pipeline lõi | ☐ | ☐ | ☐ |

### 14.2 Pipeline Stages (Mục 2)

| # | Stage | Purpose/Input/Output/Owner/Invariant đầy đủ và đúng thứ tự | PASS | FAIL | N/A |
|---|---|---|---|---|---|
| 2.1 | Narration | Bất biến trong lượt chạy, không bị pipeline sửa | ☐ | ☐ | ☐ |
| 2.2 | Semantic Extraction | Mọi phần tử neo vào span hợp lệ | ☐ | ☐ | ☐ |
| 2.3 | Semantic Beat | Phủ 100% narration, không chồng lấn | ☐ | ☐ | ☐ |
| 2.4 | Visual Obligation | Không phải scene/prompt/template; có evidence | ☐ | ☐ | ☐ |
| 2.5 | Shot Planning | Không tạo shot thừa để tăng clip count | ☐ | ☐ | ☐ |
| 2.6 | Continuity Planning | Là tầng duy nhất quản lý trạng thái xuyên-beat | ☐ | ☐ | ☐ |
| 2.7 | Scene Planning | 100% vật thể có nhãn nguồn gốc hợp lệ | ☐ | ☐ | ☐ |
| 2.8 | Prompt Composition | Không tạo semantic/continuity mới | ☐ | ☐ | ☐ |
| 2.9 | Independent QA | Độc lập theo cả 3 chiều (tác nhân/phiên/căn cứ) | ☐ | ☐ | ☐ |
| 2.10 | Final Prompt | Chỉ tồn tại sau QA PASS | ☐ | ☐ | ☐ |

### 14.3 Data Model (Mục 3)

| # | Contract | PASS | FAIL | N/A |
|---|---|---|---|---|
| 3.1 | Mọi Semantic Beat có `source_span` không rỗng, không beat nào thiếu evidence | ☐ | ☐ | ☐ |
| 3.2 | Mọi Visual Obligation có evidence, không nhầm lẫn với scene/prompt/template | ☐ | ☐ | ☐ |
| 3.3 | Mọi Shot Plan có `evidence_represented` không rỗng, không có shot dư thừa | ☐ | ☐ | ☐ |
| 3.4 | Continuity State quản lý đủ 6 hạng mục (characters/objects/locations/timeline/unresolved_actions/dependencies) | ☐ | ☐ | ☐ |
| 3.5 | Prompt chỉ chứa nội dung truy vết được từ Scene Planning, không quyết định nội dung mới | ☐ | ☐ | ☐ |
| 3.6 | QA Result có đủ 8 trường (không chỉ PASS/FAIL) | ☐ | ☐ | ☐ |

### 14.4 Traceability & Information Preservation (Mục 4–5)

| # | Yêu cầu | PASS | FAIL | N/A |
|---|---|---|---|---|
| 4.1 | 100% Final Prompt truy vết được đầy đủ chuỗi Prompt→Shot→Visual Obligation→Semantic Beat→Narration Span | ☐ | ☐ | ☐ |
| 4.2 | Output mất trace bị loại trước khi vào đánh giá chất lượng khác | ☐ | ☐ | ☐ |
| 5.1 | `meaning`/`causal_relation`/`entity_identity` không bị hạ cấp thành generic mood/symbolism/scene | ☐ | ☐ | ☐ |

### 14.5 Scene Identity & Continuity (Mục 6–7)

| # | Yêu cầu | PASS | FAIL | N/A |
|---|---|---|---|---|
| 6.1 | Scene Concept xác định bởi subject+action+setting+narrative_purpose, không bởi camera/lighting/wording | ☐ | ☐ | ☐ |
| 6.2 | Scene Fingerprint bất biến với wording/trình bày, nhạy với thay đổi danh tính | ☐ | ☐ | ☐ |
| 6.3 | So sánh Scene Fingerprint thực hiện toàn cục, có Episode Memory tích luỹ | ☐ | ☐ | ☐ |
| 7.1 | Mọi entity tuân theo vòng đời introduced→active→referenced→resolved | ☐ | ☐ | ☐ |
| 7.2 | Không có spontaneous appearance / unexplained disappearance / impossible timeline | ☐ | ☐ | ☐ |

### 14.6 Composition & QA (Mục 8–10)

| # | Yêu cầu | PASS | FAIL | N/A |
|---|---|---|---|---|
| 8.1 | Prompt Composer không tạo semantic/continuity/symbolism/props/narrative mới | ☐ | ☐ | ☐ |
| 9.1 | QA không đọc internal reasoning/self-reported coverage/self-generated checklist | ☐ | ☐ | ☐ |
| 9.2 | QA chỉ dùng narration/semantic beat/shot/final prompt làm căn cứ | ☐ | ☐ | ☐ |
| 9.3 | 6 loại lỗi (semantic mismatch/hallucination/repetition/continuity/grammar/evidence) được định nghĩa tường minh, không ngầm hiểu | ☐ | ☐ | ☐ |
| 10.1 | Acceptance criteria cho Semantic/Uniqueness/Continuity/Traceability được áp dụng đúng như Mục 10 | ☐ | ☐ | ☐ |

### 14.7 Forbidden Behaviors (Mục 11)

| # | Anti-pattern bị loại trừ | PASS | FAIL | N/A |
|---|---|---|---|---|
| 11.1 | Không có generic filler | ☐ | ☐ | ☐ |
| 11.2 | Không có template cycling | ☐ | ☐ | ☐ |
| 11.3 | Không có scene pool fallback | ☐ | ☐ | ☐ |
| 11.4 | Không có modulo selection | ☐ | ☐ | ☐ |
| 11.5 | Không có hash-based uniqueness | ☐ | ☐ | ☐ |
| 11.6 | Không có wording uniqueness | ☐ | ☐ | ☐ |
| 11.7 | Không có hallucinated props | ☐ | ☐ | ☐ |
| 11.8 | Không có fake continuity | ☐ | ☐ | ☐ |
| 11.9 | Không có self-certification QA | ☐ | ☐ | ☐ |
| 11.10 | Không có coverage-copy tautology | ☐ | ☐ | ☐ |
| 11.11 | Không có batch-blind QA | ☐ | ☐ | ☐ |
| 11.12 | Không có undocumented pipeline vocabulary | ☐ | ☐ | ☐ |

### 14.8 Domain Independence (Mục 13)

| # | Yêu cầu | PASS | FAIL | N/A |
|---|---|---|---|---|
| 13.1 | Pipeline lõi (Mục 2–12) không chứa logic đặc thù riêng cho một domain/episode cụ thể | ☐ | ☐ | ☐ |
| 13.2 | Mọi ràng buộc đặc thù domain nằm ở lớp phụ trợ (`forbidden_hallucination`, ràng buộc trình bày ở Mục 8), không sửa cấu trúc lõi | ☐ | ☐ | ☐ |

**Kết luận nghiệm thu:** Một implementation chỉ được coi là **tuân thủ specification** khi toàn bộ các dòng ở Mục 14.1–14.8 là `PASS` hoặc `NOT APPLICABLE` có lý do giải trình rõ ràng — không có dòng `FAIL` nào còn tồn tại chưa xử lý.
