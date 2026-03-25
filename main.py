from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
users_db ={}
# 🔥 THE 10-MARKS DETAILED DATABASE (Part 1: First 4 Subjects)
qa_database = {
    "DBMS": [
        {
            "q": "Q1. Explain Normalization in DBMS. Discuss 1NF, 2NF, 3NF, and BCNF in detail with examples. (10 Marks)", 
            "a": """
            <h3>1. Introduction to Normalization</h3>
            <p>Normalization is a systematic and formal approach of decomposing tables to eliminate data redundancy (repetition) and undesirable characteristics like Insertion, Update, and Deletion Anomalies. The primary objective is to divide larger tables into smaller, manageable tables and link them using relationships (Primary and Foreign keys).</p>
            
            <h3>2. First Normal Form (1NF)</h3>
            <p>A relation is in 1NF if it strictly follows the rule of atomic values. An attribute (column) of a table cannot hold multiple values. It must hold only single-valued attributes.</p>
            <ul>
                <li><b>Example:</b> If a 'Student' table has a 'Phone_Numbers' column with two numbers for one student (e.g., 98765..., 91234...), it violates 1NF. To fix this, we create separate rows for each phone number, ensuring atomicity.</li>
            </ul>

            <h3>3. Second Normal Form (2NF)</h3>
            <p>A relation is in 2NF if it satisfies 1NF and completely removes partial dependencies.</p>
            <ul>
                <li><b>Rule:</b> All non-prime attributes (attributes not part of the candidate key) must be fully functionally dependent on the entire primary key.</li>
                <li><b>Explanation:</b> If a table has a composite primary key (e.g., Student_ID + Course_ID), a non-prime attribute like 'Course_Fee' should depend on the FULL key, not just a part of it (Course_ID). If it depends on a part, it is a partial dependency and must be removed to a new table.</li>
            </ul>

            <h3>4. Third Normal Form (3NF)</h3>
            <p>A relation is in 3NF if it satisfies 2NF and removes transitive dependencies.</p>
            <ul>
                <li><b>Rule:</b> Non-prime attributes must not depend on other non-prime attributes. For any functional dependency X &rarr; Y, either X must be a Super Key, or Y must be a Prime Attribute.</li>
                <li><b>Example:</b> In an 'Employee' table, if Emp_ID determines Dept_ID, and Dept_ID determines Dept_Location, then Emp_ID transitively determines Dept_Location. This violates 3NF. We must separate Department details into a new table.</li>
            </ul>
            """
        },
        {
            "q": "Q2. What are ACID properties in a Database? Explain the Concept of Serializability. (10 Marks)",
            "a": """
            <h3>1. Introduction to Transactions</h3>
            <p>A transaction is a single logical unit of work that accesses and possibly modifies the contents of a database. To maintain data integrity during concurrent executions, a transaction must follow the ACID properties.</p>
            
            <h3>2. The ACID Properties</h3>
            <ul>
                <li><b>Atomicity (All or Nothing):</b> Ensures that all operations within the work unit are completed successfully. If not, the transaction is aborted at the point of failure and all previous operations are rolled back to their former state.</li>
                <li><b>Consistency:</b> Ensures that the database properly changes states upon a successfully committed transaction. The database must satisfy all rules and constraints before and after the transaction.</li>
                <li><b>Isolation:</b> Enables transactions to operate independently of and transparent to each other. Even if multiple transactions are running concurrently, the end result must be exactly as if they were executed sequentially.</li>
                <li><b>Durability:</b> Ensures that the result or effect of a committed transaction persists in case of a system failure. The updates are saved in non-volatile memory.</li>
            </ul>

            <h3>3. Serializability</h3>
            <p>When multiple transactions execute concurrently, it can lead to inconsistent database states (e.g., Lost Updates, Dirty Reads). Serializability is the concept of ensuring that a concurrent schedule of transactions produces the exact same result as if the transactions were executed serially (one after another).</p>
            <ul>
                <li><b>Conflict Serializability:</b> A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.</li>
                <li><b>View Serializability:</b> A less strict form of serializability ensuring that the 'view' of the database during execution is consistent with some serial schedule.</li>
            </ul>
            """
        },
        {
            "q": "Q3. Explain the Architecture of DBMS (1-Tier, 2-Tier, and 3-Tier). (10 Marks)",
            "a": """
            <h3>1. Introduction to DBMS Architecture</h3>
            <p>The architecture of a DBMS determines how the database interacts with users and applications. It is deeply influenced by the underlying computer system and network setup. The most widely used architectures are 1-tier, 2-tier, and 3-tier.</p>

            <h3>2. 1-Tier Architecture</h3>
            <p>In this simplest architecture, the database is directly available to the user. Any changes done here directly reflect on the database itself.</p>
            <ul>
                <li><b>Usage:</b> Mostly used for local application development where the programmer directly interacts with the database (e.g., MS Access, SQLite).</li>
                <li><b>Pros & Cons:</b> Very fast and easy to setup, but lacks security, scalability, and network capabilities.</li>
            </ul>

            <h3>3. 2-Tier Architecture (Client-Server)</h3>
            <p>This architecture is similar to a basic client-server model. The application on the client machine communicates directly with the database system on the server machine.</p>
            <ul>
                <li><b>How it works:</b> The user interface and application programs are on the client side. The database system runs on the server. APIs like ODBC and JDBC are used for connection.</li>
                <li><b>Pros & Cons:</b> Better security and multi-user support than 1-tier. However, if the number of clients increases exponentially, the server can become a bottleneck (scalability issue).</li>
            </ul>

            <h3>4. 3-Tier Architecture</h3>
            <p>This is the most common and secure architecture used for web applications. It adds an intermediate layer (Application Server) between the user and the database.</p>
            <ul>
                <li><b>Presentation Layer (Client):</b> The front-end user interface (e.g., Web Browser).</li>
                <li><b>Application Layer (Business Logic):</b> The middle tier containing the business logic (e.g., a Python/Flask server). It processes user inputs before passing them to the DB.</li>
                <li><b>Database Layer:</b> The back-end where the actual data resides.</li>
                <li><b>Pros:</b> Highly secure (clients cannot access DB directly), highly scalable, and easier to maintain.</li>
            </ul>
            """
        },
        {
            "q": "Q4. Differentiate between SQL and NoSQL Databases. Give use cases for both. (10 Marks)",
            "a": """
            <h3>1. SQL (Relational Databases)</h3>
            <p>SQL databases are structured, relational, and use Structured Query Language for defining and manipulating data. Examples include MySQL, PostgreSQL, and Oracle.</p>
            <ul>
                <li><b>Schema:</b> They have a predefined, rigid schema. You must define the table structure before inserting data.</li>
                <li><b>Structure:</b> Data is stored in tables consisting of rows and columns.</li>
                <li><b>Scaling:</b> Vertically scalable (scaling up by adding more CPU, RAM, or SSD to a single server).</li>
                <li><b>Properties:</b> Follows strict ACID properties, ensuring high data integrity.</li>
                <li><b>Use Cases:</b> Ideal for complex queries, financial systems, ERPs, and applications where data relationships are complex and rigid.</li>
            </ul>

            <h3>2. NoSQL (Non-Relational Databases)</h3>
            <p>NoSQL databases are non-tabular and store data differently than relational tables. Examples include MongoDB, Cassandra, and Redis.</p>
            <ul>
                <li><b>Schema:</b> They have a dynamic schema for unstructured data. Documents can have different structures.</li>
                <li><b>Structure:</b> Data can be stored as Document-based (JSON), Key-Value pairs, Wide-column, or Graph databases.</li>
                <li><b>Scaling:</b> Horizontally scalable (scaling out by adding more servers to the database cluster).</li>
                <li><b>Properties:</b> Follows the CAP Theorem and BASE properties (Basically Available, Soft state, Eventual consistency).</li>
                <li><b>Use Cases:</b> Ideal for big data, real-time web apps, content management systems, and rapidly changing data structures.</li>
            </ul>
            """
        }
    ],
    "Data Structures": [
        {
            "q": "Q1. Compare Arrays and Linked Lists. Discuss memory allocation, time complexities, and ideal use cases. (10 Marks)",
            "a": """
            <h3>1. Memory Allocation</h3>
            <ul>
                <li><b>Array:</b> Uses static memory allocation. The size of the array must be declared at compile time. Memory is allocated in a single, contiguous block on the stack (or heap if dynamically allocated).</li>
                <li><b>Linked List:</b> Uses dynamic memory allocation. Memory is allocated at runtime. Nodes are scattered randomly in the heap memory and linked together via pointers.</li>
            </ul>

            <h3>2. Time Complexity Comparison</h3>
            <ul>
                <li><b>Accessing Elements:</b> Array takes O(1) time because elements are accessed directly using an index. Linked List takes O(N) time because we must traverse from the head node to the desired node.</li>
                <li><b>Insertion/Deletion at Beginning:</b> Array takes O(N) because all subsequent elements must be shifted. Linked List takes O(1) as it only requires updating the head pointer.</li>
                <li><b>Insertion/Deletion at Middle:</b> Array takes O(N) due to shifting. Linked List also takes O(N) to reach the middle, but the actual insertion process is O(1).</li>
            </ul>

            <h3>3. Memory Overhead</h3>
            <ul>
                <li><b>Array:</b> No extra memory is required for pointers. However, if the array is allocated for 100 elements but only 10 are used, the remaining 90 slots represent wasted memory.</li>
                <li><b>Linked List:</b> No memory is wasted from pre-allocation. However, every single node requires extra memory to store the 'next' pointer (and 'prev' pointer in doubly linked lists).</li>
            </ul>
            
            <h3>4. Ideal Use Cases</h3>
            <p>Use Arrays when data size is known in advance and frequent random access (searching) is required. Use Linked Lists when data size is highly unpredictable, and the application requires frequent insertions and deletions.</p>
            """
        },
        {
            "q": "Q2. Explain Stack and Queue data structures. Provide real-world applications for both. (10 Marks)",
            "a": """
            <h3>1. Stack Data Structure</h3>
            <p>A Stack is a linear data structure that follows the <b>LIFO (Last In, First Out)</b> principle. This means the last element added to the stack will be the first one to be removed.</p>
            <ul>
                <li><b>Operations:</b> Push (insert), Pop (remove), Peek/Top (view top element).</li>
                <li><b>Implementation:</b> Can be implemented using Arrays or Linked Lists.</li>
                <li><b>Real-world Applications:</b>
                    <ol>
                        <li><b>Undo/Redo mechanisms</b> in text editors (Ctrl+Z uses a stack).</li>
                        <li><b>Browser History:</b> The 'Back' button uses a stack of visited URLs.</li>
                        <li><b>Function Calls:</b> Compilers use the Call Stack to manage function execution and recursion.</li>
                        <li><b>Expression Evaluation:</b> Converting Infix to Postfix notation.</li>
                    </ol>
                </li>
            </ul>

            <h3>2. Queue Data Structure</h3>
            <p>A Queue is a linear data structure that follows the <b>FIFO (First In, First Out)</b> principle. The first element added is the first one to be removed.</p>
            <ul>
                <li><b>Operations:</b> Enqueue (insert at rear), Dequeue (remove from front), Front, Rear.</li>
                <li><b>Types:</b> Simple Queue, Circular Queue, Priority Queue, Deque (Double Ended Queue).</li>
                <li><b>Real-world Applications:</b>
                    <ol>
                        <li><b>OS Task Scheduling:</b> CPU scheduling algorithms like Round Robin use queues.</li>
                        <li><b>Printer Spooling:</b> Documents sent to a printer are queued and printed in the order received.</li>
                        <li><b>Call Centers:</b> Customer service calls are placed in a queue until an executive is free.</li>
                    </ol>
                </li>
            </ul>
            """
        },
        {
            "q": "Q3. Explain Binary Search Tree (BST). Discuss its operations and time complexities. (10 Marks)",
            "a": """
            <h3>1. Introduction to Trees</h3>
            <p>Unlike Arrays and Linked Lists which are linear, a Tree is a hierarchical data structure consisting of nodes connected by edges. The topmost node is the Root.</p>

            <h3>2. What is a Binary Search Tree (BST)?</h3>
            <p>A BST is a special type of binary tree that strictly follows a specific ordering property:</p>
            <ul>
                <li>The left child of a node contains a value <b>less than</b> the node's value.</li>
                <li>The right child of a node contains a value <b>greater than</b> the node's value.</li>
                <li>This rule applies recursively to all left and right subtrees. No duplicate values are typically allowed.</li>
            </ul>

            <h3>3. BST Operations</h3>
            <ul>
                <li><b>Searching:</b> Starts at the root. If the target is less than the root, search the left subtree. If greater, search the right subtree. This halves the search space at each step.</li>
                <li><b>Insertion:</b> Follows the same logic as searching. When a null spot is found that satisfies the BST rule, the new node is inserted there.</li>
                <li><b>Deletion:</b> Has 3 cases: (1) Node has no children (just delete it). (2) Node has one child (link parent to the child). (3) Node has two children (find the In-order Successor or Predecessor, swap values, and delete).</li>
            </ul>

            <h3>4. Time Complexity</h3>
            <p>In a balanced BST, the time complexity for Search, Insert, and Delete is <b>O(log N)</b> because the tree height is logarithmic. However, in the worst-case scenario (a highly skewed tree resembling a linked list), the time complexity degrades to <b>O(N)</b>. To solve this, self-balancing trees like AVL or Red-Black trees are used.</p>
            """
        },
        {
            "q": "Q4. Explain Quick Sort algorithm. Discuss its logic, pivot selection, and time complexity. (10 Marks)",
            "a": """
            <h3>1. Introduction to Quick Sort</h3>
            <p>Quick Sort is a highly efficient, comparison-based sorting algorithm that utilizes the <b>Divide and Conquer</b> strategy. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.</p>

            <h3>2. The Partitioning Logic</h3>
            <p>The core of Quick Sort is the partition() function.</p>
            <ol>
                <li>Choose a pivot element (can be the first, last, middle, or random element).</li>
                <li>Rearrange the array so that all elements smaller than the pivot are placed to its left.</li>
                <li>All elements greater than the pivot are placed to its right.</li>
                <li>The pivot is now in its final, correct sorted position.</li>
                <li>Recursively apply this process to the left sub-array and right sub-array.</li>
            </ol>

            <h3>3. Pivot Selection Strategies</h3>
            <ul>
                <li><b>First/Last Element:</b> Easiest to implement but performs poorly (O(N^2)) on already sorted arrays.</li>
                <li><b>Random Element:</b> Selects a random index as pivot. Helps avoid the worst-case scenario.</li>
                <li><b>Median-of-Three:</b> Takes the median of the first, middle, and last elements as the pivot, offering highly consistent O(N log N) performance.</li>
            </ul>

            <h3>4. Time and Space Complexity</h3>
            <ul>
                <li><b>Best/Average Case Time:</b> O(N log N). The array is divided exactly in half each time.</li>
                <li><b>Worst Case Time:</b> O(N^2). Happens when the array is already sorted and the largest/smallest element is consistently chosen as the pivot.</li>
                <li><b>Space Complexity:</b> O(log N) due to recursive call stack. It is an In-Place sorting algorithm (requires no extra array).</li>
            </ul>
            """
        }
    ],
    "C Programming": [
        {
            "q": "Q1. Explain Dynamic Memory Allocation in C. Detail malloc(), calloc(), realloc(), and free(). (10 Marks)",
            "a": """
            <h3>1. Introduction</h3>
            <p>In C, memory can be allocated statically (at compile time) or dynamically (at runtime). Dynamic Memory Allocation allows a program to obtain exactly the amount of memory it needs while running, utilizing the Heap segment of memory.</p>

            <h3>2. malloc() - Memory Allocation</h3>
            <ul>
                <li>Allocates a single, contiguous block of memory of the specified size in bytes.</li>
                <li>It does <b>not</b> initialize the memory. The allocated space contains garbage values.</li>
                <li><b>Syntax:</b> <code>ptr = (int*) malloc(100 * sizeof(int));</code></li>
                <li>Returns a void pointer which must be typecast. Returns NULL if memory allocation fails.</li>
            </ul>

            <h3>3. calloc() - Contiguous Allocation</h3>
            <ul>
                <li>Allocates multiple blocks of memory of the same size.</li>
                <li>Unlike malloc, it automatically <b>initializes all allocated bytes to ZERO</b>.</li>
                <li><b>Syntax:</b> <code>ptr = (float*) calloc(25, sizeof(float));</code></li>
                <li>Slightly slower than malloc due to the initialization process.</li>
            </ul>

            <h3>4. realloc() and free()</h3>
            <ul>
                <li><b>realloc() (Re-allocation):</b> Used to dynamically change the size of previously allocated memory without losing existing data. If the current block cannot be extended, it allocates a new block, copies the data, and frees the old block.<br><b>Syntax:</b> <code>ptr = realloc(ptr, new_size);</code></li>
                <li><b>free():</b> Dynamically allocated memory is not automatically destroyed. The programmer must use <code>free(ptr);</code> to release the memory back to the heap. Failing to do so causes <b>Memory Leaks</b>, crashing the system over time.</li>
            </ul>
            """
        },
        {
            "q": "Q2. What is a Pointer in C? Explain Pointer Arithmetic and Array-Pointer relationship. (10 Marks)",
            "a": """
            <h3>1. Understanding Pointers</h3>
            <p>A pointer is a special variable in C that stores the memory address of another variable, rather than storing a direct data value. Pointers are incredibly powerful for passing large structures to functions, dynamic memory management, and hardware-level programming.</p>
            <p><b>Declaration:</b> <code>int *ptr;</code> (Declares a pointer to an integer).</p>
            <p><b>Operators:</b> The Address-of operator (<code>&amp;</code>) gets the memory address. The Dereference operator (<code>*</code>) accesses the value at that address.</p>

            <h3>2. Pointer Arithmetic</h3>
            <p>You can perform mathematical operations on pointers, but they work differently than normal math based on the data type's size.</p>
            <ul>
                <li><b>Increment (ptr++):</b> If <code>ptr</code> points to an integer (which takes 4 bytes), <code>ptr++</code> does not add 1 to the address. It adds 4 bytes, moving the pointer to the exactly next integer location.</li>
                <li><b>Addition/Subtraction:</b> <code>ptr + 3</code> moves the pointer forward by 3 elements (12 bytes for int).</li>
                <li><b>Pointer Subtraction:</b> Subtracting two pointers of the same array returns the number of elements between them.</li>
            </ul>

            <h3>3. Array and Pointer Relationship</h3>
            <p>Arrays and pointers are tightly linked in C. The name of an array acts as a constant pointer to its first element.</p>
            <ul>
                <li>If <code>int arr[5];</code> is declared, <code>arr</code> is equivalent to <code>&amp;arr[0]</code>.</li>
                <li>You can access array elements using pointer notation: <code>arr[i]</code> is exactly the same as <code>*(arr + i)</code>.</li>
                <li>This is why passing an array to a function actually passes a pointer, making array modifications inside the function reflect globally.</li>
            </ul>
            """
        },
        {
            "q": "Q3. Explain File Handling in C. Discuss fopen, fclose, reading, and writing modes. (10 Marks)",
            "a": """
            <h3>1. Introduction to File Handling</h3>
            <p>File handling allows C programs to store data permanently on a hard drive. Without files, all data processed by a program is lost when the program terminates (because RAM is volatile).</p>

            <h3>2. Opening and Closing Files</h3>
            <p>Files are accessed using a file pointer of type <code>FILE *</code>.</p>
            <ul>
                <li><b>fopen():</b> Used to open a file. It takes the filename and the mode of operation.<br><code>FILE *fp = fopen("data.txt", "w");</code></li>
                <li><b>fclose():</b> Flushes the buffer and closes the file, releasing system resources.<br><code>fclose(fp);</code></li>
            </ul>

            <h3>3. File Opening Modes</h3>
            <ul>
                <li><b>"r" (Read):</b> Opens a file for reading. Returns NULL if the file does not exist.</li>
                <li><b>"w" (Write):</b> Opens a file for writing. If the file exists, its contents are erased (overwritten). If not, a new file is created.</li>
                <li><b>"a" (Append):</b> Opens a file to append data at the end without erasing existing contents.</li>
                <li><b>"r+", "w+", "a+":</b> Extended modes that allow both reading and writing simultaneously.</li>
            </ul>

            <h3>4. Reading and Writing Functions</h3>
            <ul>
                <li><b>fprintf() & fscanf():</b> Used for formatted text I/O, exactly like printf and scanf but for files.</li>
                <li><b>fputc() & fgetc():</b> Used for reading/writing a single character at a time.</li>
                <li><b>fwrite() & fread():</b> Used for binary file handling (like storing struct objects directly into a .dat or .bin file).</li>
            </ul>
            """
        },
        {
            "q": "Q4. Difference between Structures (struct) and Unions in C. (10 Marks)",
            "a": """
            <h3>1. Introduction to User-Defined Types</h3>
            <p>Both Structures and Unions are user-defined data types in C that allow combining different primitive data types (like int, float, char) under a single name. However, they manage memory in fundamentally different ways.</p>

            <h3>2. Structures (struct)</h3>
            <p>A structure allocates separate memory space for each of its members.</p>
            <ul>
                <li><b>Memory Allocation:</b> The total size of a struct is the sum of the sizes of all its members (plus padding for alignment).</li>
                <li><b>Access:</b> You can access and assign values to all members simultaneously without data corruption.</li>
                <li><b>Usage:</b> Used when all member variables need to store data at the same time (e.g., storing a Student's Name, Roll No, and Marks).</li>
                <li><b>Syntax:</b> <code>struct Student { int roll; float marks; };</code></li>
            </ul>

            <h3>3. Unions (union)</h3>
            <p>A union allocates a single, shared memory block for all its members.</p>
            <ul>
                <li><b>Memory Allocation:</b> The total size of a union is equal to the size of its LARGEST member.</li>
                <li><b>Access:</b> You can only store a value in ONE member at a time. If you assign a value to a new member, the previous member's data is overwritten and corrupted.</li>
                <li><b>Usage:</b> Used when memory conservation is critical (embedded systems) and you know that only one attribute will be active at any given time.</li>
                <li><b>Syntax:</b> <code>union Data { int i; float f; char str[20]; };</code> (Size will be 20 bytes).</li>
            </ul>
            """
        }
    ],
    "C++ Programming": [
        {
            "q": "Q1. Explain the 4 main pillars of Object-Oriented Programming (OOP) in C++. (10 Marks)",
            "a": """
            <h3>1. Introduction to OOP</h3>
            <p>Object-Oriented Programming designs software around real-world 'objects' that contain both data (attributes) and methods (functions). It provides a clear structure and makes code easier to maintain.</p>
            
            <h3>2. Encapsulation (Data Hiding)</h3>
            <p><b>Definition:</b> The process of binding data variables and the functions that manipulate them together into a single unit (a class).</p>
            <ul>
                <li>It prevents outside interference and misuse. In C++, this is achieved using access specifiers like <code>private</code>, <code>protected</code>, and <code>public</code>.</li>
                <li><b>Analogy:</b> A capsule contains various medicines inside a single shell.</li>
            </ul>
            
            <h3>3. Abstraction (Implementation Hiding)</h3>
            <p><b>Definition:</b> Displaying only the essential information to the user and hiding the complex background details.</p>
            <ul>
                <li>In C++, this is achieved using interfaces, abstract classes (pure virtual functions), and header files.</li>
                <li><b>Analogy:</b> Driving a car. You press the accelerator to speed up; you don't need to know the complex internal combustion process of the engine.</li>
            </ul>
            
            <h3>4. Inheritance (Code Reusability)</h3>
            <p><b>Definition:</b> The mechanism where a new class (Derived Class) acquires the properties and behaviors of an existing class (Base Class).</p>
            <ul>
                <li>It prevents rewriting code. Types include Single, Multiple, Multilevel, and Hierarchical inheritance.</li>
                <li><b>Analogy:</b> A child inheriting genetic traits from parents.</li>
            </ul>
            
            <h3>5. Polymorphism (Many Forms)</h3>
            <p><b>Definition:</b> The ability of a message, function, or operator to be displayed or behave differently based on the context.</p>
            <ul>
                <li>Achieved via Compile-Time Polymorphism (Function/Operator Overloading) and Run-Time Polymorphism (Virtual Functions).</li>
                <li><b>Analogy:</b> A person acts as a student in college, a son at home, and a customer at a mall.</li>
            </ul>
            """
        },
        {
            "q": "Q2. What is Polymorphism? Differentiate between Compile-time and Run-time Polymorphism. (10 Marks)",
            "a": """
            <h3>1. Concept of Polymorphism</h3>
            <p>Polymorphism comes from Greek words meaning "many forms". In C++, it means that a single function name or operator can behave differently depending on the types of arguments or objects passed to it.</p>

            <h3>2. Compile-Time Polymorphism (Early Binding / Static Binding)</h3>
            <p>In this type, the compiler determines which function to execute during the compilation phase. It is faster but less flexible.</p>
            <ul>
                <li><b>Function Overloading:</b> Creating multiple functions with the same name but different parameters (number or type of arguments). The compiler checks the arguments to resolve the call.<br>
                <i>Example:</i> <code>add(int, int)</code> vs <code>add(double, double)</code>.</li>
                <li><b>Operator Overloading:</b> Redefining the way standard operators (like +, -, *) work for user-defined classes. For example, using the '+' operator to concatenate two custom String objects.</li>
            </ul>

            <h3>3. Run-Time Polymorphism (Late Binding / Dynamic Binding)</h3>
            <p>In this type, the compiler cannot determine the function call at compile time. The resolution happens during program execution using pointers.</p>
            <ul>
                <li><b>Virtual Functions:</b> This is achieved through Inheritance and Function Overriding. A base class declares a function using the <code>virtual</code> keyword. The derived class overrides this function.</li>
                <li><b>How it works:</b> When a Base class pointer holds the address of a Derived class object and calls the virtual function, C++ checks the actual object type at runtime and executes the Derived class's function.</li>
                <li>Provides immense flexibility for building dynamic systems, though it carries a slight performance overhead due to the V-Table (Virtual Table) lookup.</li>
            </ul>
            """
        },
        {
            "q": "Q3. Explain Constructors and Destructors in C++. Discuss the types of Constructors. (10 Marks)",
            "a": """
            <h3>1. Constructors</h3>
            <p>A Constructor is a special member function of a class that is executed automatically whenever an object of that class is created. Its primary purpose is to initialize the object's data members.</p>
            <ul>
                <li>It has exactly the same name as the class.</li>
                <li>It does not have a return type, not even <code>void</code>.</li>
                <li>It is usually declared in the <code>public</code> section.</li>
            </ul>

            <h3>2. Types of Constructors</h3>
            <ul>
                <li><b>Default Constructor:</b> Takes no arguments. If you don't define any constructor, C++ generates a blank default constructor automatically.<br><code>Student() { marks = 0; }</code></li>
                <li><b>Parameterized Constructor:</b> Takes arguments, allowing you to initialize objects with specific values at the time of creation.<br><code>Student(int m) { marks = m; }</code></li>
                <li><b>Copy Constructor:</b> Initializes a new object using an existing object of the same class. Crucial when deep copying dynamically allocated memory is required.<br><code>Student(const Student &obj) { marks = obj.marks; }</code></li>
            </ul>

            <h3>3. Destructors</h3>
            <p>A Destructor is a special member function executed automatically when an object goes out of scope or is explicitly deleted. Its purpose is to free up resources (like closing files or freeing heap memory).</p>
            <ul>
                <li>It has the same name as the class, prefixed with a tilde (<code>~</code>).</li>
                <li>It takes NO arguments and has NO return type. There can be only one destructor per class.<br><code>~Student() { cout << "Object destroyed"; }</code></li>
            </ul>
            """
        },
        {
            "q": "Q4. What is Exception Handling in C++? Explain try, catch, and throw mechanisms. (10 Marks)",
            "a": """
            <h3>1. Introduction to Exception Handling</h3>
            <p>An exception is an unexpected problem that arises during the execution of a program (Runtime Error), such as division by zero, accessing an out-of-bounds array index, or running out of memory. Exception handling allows a program to deal with these errors gracefully without crashing abruptly.</p>

            <h3>2. The Three Keywords</h3>
            <p>C++ uses three keywords to implement this mechanism: <b>try, throw, and catch</b>.</p>

            <ul>
                <li><b>try block:</b> This block contains the code that might generate an exception. It acts as a monitoring area. If an error occurs inside the try block, an exception is thrown.</li>
                <li><b>throw keyword:</b> When a problem is detected, the program uses the <code>throw</code> keyword to signal that an error has occurred. You can throw built-in types (like int or string) or custom objects.</li>
                <li><b>catch block:</b> This block immediately follows the try block. It "catches" the exception thrown and contains the logic to handle the error (e.g., displaying an error message to the user).</li>
            </ul>

            <h3>3. Example Flow</h3>
            <pre><code>
try {
    int denominator = 0;
    if (denominator == 0) {
        throw "Division by zero error!"; // Throws a string
    }
    int result = 10 / denominator;
} 
catch (const char* errorMessage) {
    cout << "Exception Caught: " << errorMessage;
}
            </code></pre>
            
            <h3>4. Advantages</h3>
            <p>Separates error-handling code from normal logic code, making the program cleaner. Ensures the program continues running or terminates safely rather than crashing the OS process.</p>
            """
        }
    ]
}
# 🔥 PART 2: THE 10-MARKS DETAILED DATABASE (Next 4 Subjects)
# Ye update() function purane database mein in naye subjects ko automatically jod dega!
qa_database.update({
    "Web Development": [
        {
            "q": "Q1. Differentiate between HTML4 and HTML5. Explain the importance of Semantic Tags. (10 Marks)",
            "a": """
            <h3>1. Introduction to HTML5</h3>
            <p>HTML5 is the latest major revision of the core language of the World Wide Web. It introduced new elements, attributes, and behaviors, specifically focusing on multimedia and mobile device support without requiring external plugins like Flash.</p>

            <h3>2. Key Differences (HTML4 vs HTML5)</h3>
            <ul>
                <li><b>Multimedia:</b> HTML4 required plugins (like Adobe Flash or Silverlight) to play audio and video. HTML5 introduced built-in <code>&lt;audio&gt;</code> and <code>&lt;video&gt;</code> tags.</li>
                <li><b>Storage:</b> HTML4 strictly used Cookies to store small amounts of data. HTML5 introduced LocalStorage and SessionStorage, allowing up to 10MB of data storage directly in the browser.</li>
                <li><b>Graphics:</b> HTML4 lacked native vector graphics support. HTML5 introduced the <code>&lt;canvas&gt;</code> element for 2D drawing and native support for SVG (Scalable Vector Graphics).</li>
                <li><b>Doctype:</b> HTML4 had a very long and complex doctype declaration. HTML5 simplified it to just <code>&lt;!DOCTYPE html&gt;</code>.</li>
            </ul>

            <h3>3. Semantic Tags in HTML5</h3>
            <p>Semantic HTML means using HTML markup to reinforce the meaning of the information in webpages, rather than merely defining its presentation.</p>
            <ul>
                <li><b>Examples:</b> <code>&lt;header&gt;</code>, <code>&lt;footer&gt;</code>, <code>&lt;article&gt;</code>, <code>&lt;section&gt;</code>, <code>&lt;nav&gt;</code>.</li>
                <li><b>Importance for SEO:</b> Search engine crawlers (like Googlebot) easily understand the page structure, improving search rankings.</li>
                <li><b>Accessibility:</b> Screen readers for visually impaired users can navigate the webpage logically using these tags.</li>
            </ul>
            """
        },
        {
            "q": "Q2. Explain the CSS Box Model in detail with a proper diagrammatic explanation. (10 Marks)",
            "a": """
            <h3>1. What is the CSS Box Model?</h3>
            <p>In CSS, the term "Box Model" is used when talking about design and layout. The CSS box model is essentially a box that wraps around every HTML element. It determines the space the element takes on the screen and how it interacts with other elements.</p>

            <h3>2. Components of the Box Model (From Inside to Outside)</h3>
            <ul>
                <li><b>1. Content:</b> The innermost part. This is where the actual text, images, or child elements appear. Its size is controlled by the <code>width</code> and <code>height</code> properties.</li>
                <li><b>2. Padding:</b> The transparent area immediately surrounding the content. It creates space <i>inside</i> the element's border. The background color of the element extends into the padding area.</li>
                <li><b>3. Border:</b> A visible line that wraps around the padding and content. You can set its thickness, style (solid, dashed), and color.</li>
                <li><b>4. Margin:</b> The outermost layer. It creates transparent space <i>outside</i> the border to push other elements away. Margins of adjacent elements can sometimes collapse into a single margin.</li>
            </ul>

            <h3>3. Calculation of Total Element Width</h3>
            <p>By default (when <code>box-sizing: content-box</code> is used), the total width an element occupies on the screen is calculated as:</p>
            <p><b>Total Width</b> = Content Width + Left Padding + Right Padding + Left Border + Right Border + Left Margin + Right Margin.</p>
            
            <h3>4. The box-sizing Property (The Modern Fix)</h3>
            <p>Calculating widths manually is tedious. Modern web development uses <code>box-sizing: border-box;</code>. This forces the padding and border to be included <i>inside</i> the specified width and height, preventing the element from expanding and breaking layouts.</p>
            """
        },
        {
            "q": "Q3. Explain CSS Flexbox vs CSS Grid. When should you use which? (10 Marks)",
            "a": """
            <h3>1. CSS Flexbox (Flexible Box Layout)</h3>
            <p>Flexbox is a <b>One-Dimensional</b> layout system. It is designed to lay out items in a single direction—either in a row (horizontally) or in a column (vertically).</p>
            <ul>
                <li><b>Key Properties:</b> <code>display: flex;</code>, <code>justify-content</code> (aligns items along the main axis), <code>align-items</code> (aligns items along the cross axis), <code>flex-wrap</code>.</li>
                <li><b>Best For:</b> Aligning elements inside a container, distributing space evenly, creating navigation bars, and aligning items perfectly in the center of a div.</li>
            </ul>

            <h3>2. CSS Grid Layout</h3>
            <p>CSS Grid is a <b>Two-Dimensional</b> layout system. It can handle both rows and columns simultaneously, giving you complete control over complex webpage structures.</p>
            <ul>
                <li><b>Key Properties:</b> <code>display: grid;</code>, <code>grid-template-columns</code>, <code>grid-template-rows</code>, <code>grid-gap</code>.</li>
                <li><b>Best For:</b> Building the macro-structure of a webpage (like the overall layout with a header, sidebar, main content area, and footer), creating image galleries, and overlapping elements.</li>
            </ul>

            <h3>3. When to use which?</h3>
            <p>Flexbox is content-first (the size of items dictates the layout), while Grid is layout-first (the grid tracks dictate the size of items). The standard modern practice is to use <b>CSS Grid for the overall page layout</b> and <b>Flexbox for the components inside those grid areas</b>.</p>
            """
        },
        {
            "q": "Q4. Explain RESTful APIs. What are the common HTTP Methods used? (10 Marks)",
            "a": """
            <h3>1. What is a RESTful API?</h3>
            <p>REST stands for Representational State Transfer. It is a software architectural style that defines a set of constraints for creating web services. A RESTful API allows client applications to communicate with server applications over the internet using standard HTTP protocols.</p>

            <h3>2. Key Principles of REST</h3>
            <ul>
                <li><b>Statelessness:</b> The server does not store any state about the client session on the server side. Every request from the client must contain all the information necessary to understand and process it.</li>
                <li><b>Client-Server Architecture:</b> The user interface (client) is completely separated from the data storage (server), allowing them to evolve independently.</li>
                <li><b>Uniform Interface:</b> Resources (data) are identified uniquely via URLs (Uniform Resource Locators) and manipulated using standard HTTP methods.</li>
            </ul>

            <h3>3. Common HTTP Methods (CRUD Operations)</h3>
            <ul>
                <li><b>GET (Read):</b> Requests data from a specified resource. It should never modify data. (e.g., getting a list of students).</li>
                <li><b>POST (Create):</b> Submits data to be processed to a specified resource, often resulting in a change in state or creation of a new resource on the server.</li>
                <li><b>PUT (Update):</b> Updates a current resource with new data. It completely replaces the existing resource.</li>
                <li><b>PATCH (Partial Update):</b> Applies partial modifications to a resource (e.g., just updating a user's password).</li>
                <li><b>DELETE (Delete):</b> Deletes the specified resource from the server.</li>
            </ul>
            """
        }
    ],
    "JavaScript": [
        {
            "q": "Q1. Explain the differences between var, let, and const in JavaScript. What is Hoisting? (10 Marks)",
            "a": """
            <h3>1. Introduction</h3>
            <p>Before ES6 (2015), JavaScript only had <code>var</code> for variable declaration. ES6 introduced <code>let</code> and <code>const</code> to solve scoping issues and make code more predictable.</p>

            <h3>2. Scope Differences</h3>
            <ul>
                <li><b>var (Function Scope):</b> Variables declared with <code>var</code> are scoped to the immediate function body. If declared outside a function, they become global variables attached to the <code>window</code> object.</li>
                <li><b>let (Block Scope):</b> Scoped to the immediate enclosing block (e.g., inside an <code>if</code> statement or a <code>for</code> loop). It does not leak outside the block.</li>
                <li><b>const (Block Scope):</b> Similar to <code>let</code>, but the variable cannot be reassigned once initialized. However, if the <code>const</code> holds an object or array, its properties/elements CAN be mutated.</li>
            </ul>

            <h3>3. Hoisting and Temporal Dead Zone (TDZ)</h3>
            <p><b>Hoisting</b> is JavaScript's default behavior of moving declarations to the top of the current scope before code execution.</p>
            <ul>
                <li><code>var</code> variables are hoisted and initialized with <code>undefined</code>. You can use them before declaration without an error (though it yields <code>undefined</code>).</li>
                <li><code>let</code> and <code>const</code> are also hoisted, but they are NOT initialized. They are placed in a <b>Temporal Dead Zone (TDZ)</b> from the start of the block until the declaration line. Accessing them before declaration throws a <code>ReferenceError</code>.</li>
            </ul>
            """
        },
        {
            "q": "Q2. Explain Closures in JavaScript with a practical example. (10 Marks)",
            "a": """
            <h3>1. What is a Closure?</h3>
            <p>A closure is a feature in JavaScript where an inner function has access to the outer (enclosing) function's variables—a scope chain. Crucially, the inner function remembers these variables even after the outer function has finished executing and returned.</p>

            <h3>2. The Three Scope Chains</h3>
            <p>A closure has access to three scopes:</p>
            <ol>
                <li>Its own local scope (variables defined between its curly brackets).</li>
                <li>Outer function's scope (variables of the function that wraps it).</li>
                <li>Global scope.</li>
            </ol>

            <h3>3. Practical Example: Data Privacy</h3>
            <p>JavaScript did not traditionally have private variables. Closures allow us to emulate private variables.</p>
            <pre><code>
function createCounter() {
    let count = 0; // 'count' is a private variable
    
    return function() { // This inner function is a closure
        count++;
        return count;
    };
}

const counterA = createCounter();
console.log(counterA()); // Output: 1
console.log(counterA()); // Output: 2
            </code></pre>
            <p>Here, the inner function maintains access to <code>count</code>, but there is no way for the outside world to access or modify <code>count</code> directly except through the returned function.</p>

            <h3>4. Use Cases</h3>
            <p>Closures are widely used in Event Handlers, Callbacks, Currying, and Module design patterns to maintain state without polluting the global scope.</p>
            """
        },
        {
            "q": "Q3. What are Promises in JavaScript? Explain async/await. (10 Marks)",
            "a": """
            <h3>1. The Problem with Callbacks</h3>
            <p>Historically, asynchronous operations (like fetching data from an API) were handled using Callback functions. However, multiple nested callbacks led to unreadable and unmaintainable code, known as <b>Callback Hell</b> or the Pyramid of Doom.</p>

            <h3>2. Introduction to Promises</h3>
            <p>A Promise is an object representing the eventual completion (or failure) of an asynchronous operation and its resulting value. It acts as a proxy for a value not necessarily known when the promise is created.</p>
            <p><b>Three States of a Promise:</b></p>
            <ul>
                <li><b>Pending:</b> Initial state, neither fulfilled nor rejected.</li>
                <li><b>Fulfilled:</b> The operation completed successfully (handled via <code>.then()</code>).</li>
                <li><b>Rejected:</b> The operation failed (handled via <code>.catch()</code>).</li>
            </ul>

            <h3>3. Async / Await (Syntactic Sugar)</h3>
            <p>Introduced in ES8, <code>async/await</code> makes asynchronous code look and behave a little more like synchronous code, making it much easier to read and debug.</p>
            <ul>
                <li><b>async:</b> Placing the word <code>async</code> before a function makes it always return a Promise.</li>
                <li><b>await:</b> Can only be used inside an <code>async</code> function. It makes JavaScript wait until that Promise settles and returns its result.</li>
            </ul>
            <p><b>Error Handling:</b> Instead of <code>.catch()</code>, <code>async/await</code> uses standard <code>try...catch</code> blocks, unifying error handling for both sync and async code.</p>
            """
        },
        {
            "q": "Q4. Explain the Event Loop and how JavaScript handles asynchronous operations. (10 Marks)",
            "a": """
            <h3>1. The Single-Threaded Nature of JS</h3>
            <p>JavaScript is a synchronous, single-threaded language. It has one Call Stack, meaning it can only execute one piece of code at a time. If a function takes 10 seconds to execute, it blocks the browser entirely. To prevent this, JS uses the Event Loop.</p>

            <h3>2. Core Components</h3>
            <ul>
                <li><b>Call Stack:</b> Where functions are pushed to be executed.</li>
                <li><b>Web APIs:</b> Provided by the browser (DOM, setTimeout, fetch). They run in the background outside the JS thread.</li>
                <li><b>Macrotask Queue (Callback Queue):</b> Where callbacks from Web APIs (like setTimeout) wait to be executed.</li>
                <li><b>Microtask Queue:</b> Where Promises (like <code>.then()</code>) wait. This queue has a <b>higher priority</b> than the Macrotask queue.</li>
            </ul>

            <h3>3. How the Event Loop Works</h3>
            <ol>
                <li>When an async operation like <code>setTimeout()</code> is called, it is pushed to the Call Stack, and handed off to the Web API. The timer runs in the background.</li>
                <li>JS moves on to the next line of code synchronously.</li>
                <li>When the timer finishes, the callback function is pushed to the Macrotask Queue.</li>
                <li><b>The Event Loop's Job:</b> It continuously checks if the Call Stack is EMPTY.</li>
                <li>If the Call Stack is empty, it first empties the entire Microtask Queue. After that is clear, it takes the first task from the Macrotask Queue and pushes it to the Call Stack for execution.</li>
            </ol>
            """
        }
    ],
    "Computer Networking": [
        {
            "q": "Q1. Explain the TCP/IP Model and compare it with the OSI Model. (10 Marks)",
            "a": """
            <h3>1. Introduction to TCP/IP Model</h3>
            <p>The Transmission Control Protocol/Internet Protocol (TCP/IP) model is the practical, implemented model of the internet, unlike the OSI model which is a theoretical reference. It consists of 4 layers.</p>

            <h3>2. Layers of the TCP/IP Model</h3>
            <ul>
                <li><b>1. Network Access Layer (Link Layer):</b> Corresponds to the OSI Physical and Data Link layers. It defines how data is physically sent through the network (Ethernet, Wi-Fi, MAC addressing).</li>
                <li><b>2. Internet Layer:</b> Corresponds to the OSI Network layer. Responsible for logical transmission of packets over the network. Main protocol is IP (Internet Protocol).</li>
                <li><b>3. Transport Layer:</b> Matches the OSI Transport layer. Handles host-to-host communication, error control, and flow control. Protocols: TCP (Reliable) and UDP (Fast).</li>
                <li><b>4. Application Layer:</b> Combines OSI Session, Presentation, and Application layers. Contains higher-level protocols used by most applications (HTTP, FTP, DNS, SMTP).</li>
            </ul>

            <h3>3. Comparison with OSI Model</h3>
            <ul>
                <li>OSI has 7 layers, TCP/IP has 4 layers.</li>
                <li>OSI is a conceptual model, while TCP/IP is the actual client-server model used for the internet.</li>
                <li>In OSI, the model was developed before the protocols. In TCP/IP, protocols were developed first, and the model was just a description of them.</li>
                <li>TCP/IP strictly separates the Application layer from the transport layer but groups presentation and session duties into the Application layer.</li>
            </ul>
            """
        },
        {
            "q": "Q2. Differentiate between TCP and UDP. State their use cases. (10 Marks)",
            "a": """
            <h3>1. Overview</h3>
            <p>Both TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) operate at the Transport Layer of the OSI model. However, they serve entirely different purposes regarding reliability and speed.</p>

            <h3>2. Transmission Control Protocol (TCP)</h3>
            <ul>
                <li><b>Connection-Oriented:</b> Establishes a connection between the sender and receiver before sending data (using a 3-way handshake: SYN, SYN-ACK, ACK).</li>
                <li><b>Reliability:</b> Guarantees delivery of data. It ensures packets arrive in the correct order using sequence numbers. If a packet is lost, TCP retransmits it.</li>
                <li><b>Speed:</b> Slower due to the overhead of connection establishment, error checking, and acknowledgment mechanisms.</li>
                <li><b>Use Cases:</b> Web browsing (HTTP/HTTPS), File transfers (FTP), Emails (SMTP). Situations where data loss is unacceptable.</li>
            </ul>

            <h3>3. User Datagram Protocol (UDP)</h3>
            <ul>
                <li><b>Connectionless:</b> Sends packets directly without establishing a connection. Fire and forget.</li>
                <li><b>Unreliable:</b> Does not guarantee delivery. Packets can be dropped or arrive out of order. There is no retransmission mechanism.</li>
                <li><b>Speed:</b> Extremely fast because it lacks the heavy overhead of TCP.</li>
                <li><b>Use Cases:</b> Live Video Streaming, Online Gaming (like Valorant), VoIP/Audio calls. Situations where speed is critical and a few dropped frames won't break the system.</li>
            </ul>
            """
        },
        {
            "q": "Q3. What is an IP Address? Differentiate between IPv4 and IPv6. (10 Marks)",
            "a": """
            <h3>1. What is an IP Address?</h3>
            <p>An Internet Protocol (IP) address is a unique numerical label assigned to every device connected to a computer network that uses the IP for communication. It serves two main functions: identifying the host (or network interface) and providing the location of the host in the network.</p>

            <h3>2. IPv4 (Internet Protocol Version 4)</h3>
            <ul>
                <li><b>Size:</b> 32-bit address space.</li>
                <li><b>Format:</b> Represented in dotted-decimal notation. Example: <code>192.168.1.1</code>.</li>
                <li><b>Capacity:</b> Can support approximately 4.3 billion unique addresses, which is exhausted today due to the explosion of mobile devices and IoT.</li>
                <li><b>Configuration:</b> Often configured manually or via DHCP. Requires NAT (Network Address Translation) to allow multiple private IP devices to share one public IP.</li>
            </ul>

            <h3>3. IPv6 (Internet Protocol Version 6)</h3>
            <ul>
                <li><b>Size:</b> 128-bit address space.</li>
                <li><b>Format:</b> Represented in hexadecimal notation, separated by colons. Example: <code>2001:0db8:85a3:0000:0000:8a2e:0370:7334</code>.</li>
                <li><b>Capacity:</b> Supports 340 undecillion addresses (practically infinite).</li>
                <li><b>Advantages:</b> Built-in security (IPsec is mandatory), no need for NAT, simpler header format for faster routing, and automatic stateless address configuration.</li>
            </ul>
            """
        },
        {
            "q": "Q4. Explain Routing in Networking. Differentiate between Distance Vector and Link State Routing. (10 Marks)",
            "a": """
            <h3>1. What is Routing?</h3>
            <p>Routing is the process of selecting a path for traffic in a network across multiple networks. It happens at Layer 3 (Network Layer) using Routers. Routers maintain routing tables to decide the best interface to forward a packet.</p>

            <h3>2. Distance Vector Routing</h3>
            <ul>
                <li><b>Concept:</b> Each router maintains a table (vector) giving the best known distance (hop count) to each destination. It determines the direction (vector) and distance.</li>
                <li><b>Information Sharing:</b> Routers share their ENTIRE routing table, but ONLY with their immediate, directly connected neighbors.</li>
                <li><b>Updates:</b> Updates are sent at regular periodic intervals (e.g., every 30 seconds).</li>
                <li><b>Algorithm:</b> Uses the Bellman-Ford algorithm. Example Protocol: RIP (Routing Information Protocol).</li>
                <li><b>Issue:</b> Prone to the "Count to Infinity" problem and routing loops due to slow convergence.</li>
            </ul>

            <h3>3. Link State Routing</h3>
            <ul>
                <li><b>Concept:</b> Every router constructs a complete map (topology) of the entire network. Each router calculates the shortest path from itself to all other nodes using this map.</li>
                <li><b>Information Sharing:</b> Routers share information about their direct links (link state) with ALL routers in the network (via flooding).</li>
                <li><b>Updates:</b> Updates are triggered ONLY when there is a topology change (like a link going down), making it highly efficient on bandwidth.</li>
                <li><b>Algorithm:</b> Uses Dijkstra's Shortest Path algorithm. Example Protocol: OSPF (Open Shortest Path First).</li>
                <li><b>Pros:</b> Fast convergence, loop-free, better for large networks.</li>
            </ul>
            """
        }
    ],
    "Computer Graphics": [
        {
            "q": "Q1. Differentiate between Raster Scan and Random Scan Displays. (10 Marks)",
            "a": """
            <h3>1. Raster Scan Displays</h3>
            <p>Raster scan is the most common technique used in modern monitors and televisions. The electron beam sweeps across the screen, one row at a time, from top to bottom.</p>
            <ul>
                <li><b>Drawing Method:</b> The image is represented as a 2D matrix of pixels. The beam sweeps across all parts of the screen regardless of whether there is an image there or not.</li>
                <li><b>Refresh Rate:</b> High refresh rate (usually 60 to 80 frames per second) to prevent flickering.</li>
                <li><b>Cost and Resolution:</b> Cheaper to produce, but resolution is limited by the pixel grid size.</li>
                <li><b>Realism:</b> Excellent for rendering highly realistic images, filled polygons, and complex shading because every pixel can have a unique color.</li>
            </ul>

            <h3>2. Random Scan Displays (Vector Displays)</h3>
            <p>In a random scan display, the electron beam is directed ONLY to the parts of the screen where a picture is to be drawn, drawing it line by line.</p>
            <ul>
                <li><b>Drawing Method:</b> Uses mathematical commands to draw lines from one point to another. It does not scan the blank areas.</li>
                <li><b>Refresh Rate:</b> Depends on the complexity of the image. Too many lines can cause flickering.</li>
                <li><b>Cost and Resolution:</b> Higher resolution since lines are drawn continuously without pixelation (no jagged edges).</li>
                <li><b>Realism:</b> Cannot easily display complex realistic images with shading. It is mainly used for engineering drawings, architecture, and old arcade games like Asteroids.</li>
            </ul>
            """
        },
        {
            "q": "Q2. Explain the basic 2D Transformations: Translation, Rotation, and Scaling. Provide transformation matrices. (10 Marks)",
            "a": """
            <h3>1. Introduction to 2D Transformations</h3>
            <p>Transformation is the process of altering the coordinate descriptions of objects. It is used to reposition, resize, or reorient objects on the screen. It relies heavily on matrix multiplication.</p>

            <h3>2. Translation</h3>
            <p>Translation moves an object in a straight line path from one coordinate location to another.</p>
            <ul>
                <li>We add translation distances, <b>tx</b> and <b>ty</b>, to the original coordinates (x, y) to get new coordinates (x', y').</li>
                <li>Equations: <code>x' = x + tx</code>, <code>y' = y + ty</code>.</li>
                <li>In homogeneous coordinates, it is represented as a matrix addition/multiplication.</li>
            </ul>

            <h3>3. Rotation</h3>
            <p>Rotation repositions an object along a circular path in the XY plane about an origin or pivot point by a specific angle <b>&theta;</b>.</p>
            <ul>
                <li>Positive angles generally produce counterclockwise rotation.</li>
                <li>Equations: <br><code>x' = x &middot; cos(&theta;) - y &middot; sin(&theta;)</code><br><code>y' = x &middot; sin(&theta;) + y &middot; cos(&theta;)</code>.</li>
            </ul>

            <h3>4. Scaling</h3>
            <p>Scaling alters the size of an object. This is done by multiplying the original coordinates by scaling factors <b>sx</b> and <b>sy</b>.</p>
            <ul>
                <li>If sx and sy > 1, the object enlarges. If < 1, the object shrinks.</li>
                <li>Equations: <code>x' = x &middot; sx</code>, <code>y' = y &middot; sy</code>.</li>
                <li>Note: Scaling scales the object relative to the origin, which also moves the object away from the origin unless a fixed-point scaling is used.</li>
            </ul>
            """
        },
        {
            "q": "Q3. Explain the Cohen-Sutherland Line Clipping Algorithm. (10 Marks)",
            "a": """
            <h3>1. What is Line Clipping?</h3>
            <p>Clipping is a procedure that identifies the portions of a picture that are either inside or outside a specified region of space. The region against which an object is clipped is called a clip window.</p>

            <h3>2. Cohen-Sutherland Algorithm Concept</h3>
            <p>This is a fast and efficient algorithm that divides the 2D space into 9 regions using the edges of the clipping window. Each region is assigned a 4-bit region code (TBRL - Top, Bottom, Right, Left).</p>
            <ul>
                <li>The central visible window has a code of <b>0000</b>.</li>
                <li>If a point is above the window, the Top bit is 1. If to the left, the Left bit is 1, and so on.</li>
            </ul>

            <h3>3. The Three Cases of the Algorithm</h3>
            <p>For a line connecting point P1 and P2:</p>
            <ol>
                <li><b>Trivial Acceptance:</b> If both endpoints have a region code of 0000, the line lies completely inside the window and is accepted immediately without calculation.</li>
                <li><b>Trivial Rejection:</b> If the bitwise AND operation of both region codes is NOT equal to 0000 (meaning both points share a common outside region, like both being completely above the window), the line is completely outside and is rejected immediately.</li>
                <li><b>Partial Clipping:</b> If the bitwise AND is 0000, but the points are not both 0000, the line intersects the boundary. We calculate the intersection point using the line equation <code>y = mx + c</code>, discard the outside portion, and repeat the process for the new line segment until it is fully inside or rejected.</li>
            </ol>
            """
        },
        {
            "q": "Q4. Differentiate between Flood Fill and Boundary Fill polygon filling algorithms. (10 Marks)",
            "a": """
            <h3>1. Polygon Filling</h3>
            <p>Polygon filling algorithms color the interior of a closed shape. They generally require a starting internal point known as a "seed".</p>

            <h3>2. Boundary Fill Algorithm</h3>
            <p>This algorithm is used when the polygon is defined by a distinct boundary color.</p>
            <ul>
                <li><b>Logic:</b> It starts from a seed point inside the shape. It checks neighboring pixels. If a pixel is NOT the boundary color and NOT already the fill color, it colors it with the fill color and recursively calls itself for the neighboring pixels.</li>
                <li><b>Condition:</b> Works perfectly ONLY if the entire boundary is of one single, uniform color.</li>
                <li><b>Connectivity:</b> Can be implemented using 4-connected (checks up, down, left, right) or 8-connected (checks diagonals too) methods.</li>
            </ul>

            <h3>3. Flood Fill Algorithm</h3>
            <p>This algorithm is used when the polygon area has a uniform interior color, but the boundary might be made of various different colors.</p>
            <ul>
                <li><b>Logic:</b> Instead of looking for a boundary color, it looks for the original interior color. Starting from the seed point, it replaces the 'old color' with the 'new fill color'.</li>
                <li><b>Usage:</b> This is the algorithm used by the "Paint Bucket" tool in applications like MS Paint or Photoshop.</li>
                <li><b>Difference:</b> Boundary fill stops when it hits a specific edge color. Flood fill stops when it runs out of pixels matching the original target color.</li>
            </ul>
            """
        }
    ]
})
@app.route('/')
def index():
    return render_template('login.html', error=None, success=None)

@app.route('/signup', methods=['POST'])
def signup():
    user = request.form.get('username')
    pw = request.form.get('password')
    if user in users_db:
        return render_template('login.html', error="Username already exists! ⚠️", success=None)
    else:
        users_db[user] = pw
        return render_template('login.html', error=None, success="Account created successfully! Please Login. ✅")

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')
    if user in users_db and users_db[user] == pw:
        return redirect(url_for('dashboard', username=user))
    else:
        return render_template('login.html', error="Invalid Username or Password! ❌", success=None)

@app.route('/dashboard')
def dashboard():
    user = request.args.get('username', 'Developer')
    return render_template('dashboard.html', name=user)

# 🔥 NAYA ROUTE: Dropdown menu ke liye
@app.route('/predictor', methods=['GET', 'POST'])
def predictor():
    # Database se saare subjects ki list nikal lo
    all_subjects = list(qa_database.keys())
    
    # Agar user ne dropdown se koi subject select karke button dabaya hai (POST)
    if request.method == 'POST':
        selected_subject = request.form.get('subject')
    else:
        # Jab user pehli baar page kholega (GET), toh pehla subject dikha do
        selected_subject = all_subjects[0]
        
    questions = qa_database[selected_subject]
    return render_template('predictor.html', subjects=all_subjects, current_subject=selected_subject, questions=questions)

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')