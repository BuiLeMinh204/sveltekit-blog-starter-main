<script lang="ts">
  let to = "";
  let subject = "";
  let body = "";
  let success = false;
  let error = "";

  async function sendEmail() {
    try {
      const res = await fetch("http://localhost:5000/send-email", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ to, subject, body })
      });


      const result = await res.json();
      success = res.ok;
      error = success ? "" : result.message || "Something went wrong";
    } catch (err) {
      success = false;
      error = "Error connecting to backend.";
    }
  }
</script>

<main class="container">
  <h1>📧 Send Email</h1>
  <form on:submit|preventDefault={sendEmail} class="form">
    <label>
      To:
      <input type="email" bind:value={to} required placeholder="example@mail.com" />
    </label>
    <label>
      Subject:
      <input type="text" bind:value={subject} required placeholder="Subject line" />
    </label>
    <label>
      Body:
      <textarea bind:value={body} required placeholder="Your message..."></textarea>
    </label>
    <button type="submit">Send Email</button>
  </form>

  {#if success}
    <p class="status success">✅ Email has been queued.</p>
  {:else if error}
    <p class="status error">❌ {error}</p>
  {/if}
</main>

<style>
  .container {
    max-width: 600px;
    margin: 3rem auto;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    background-color: #fff;
  }
  h1 {
    text-align: center;
    margin-bottom: 2rem;
    color: #333;
  }
  .form {
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
  }
  label {
    display: flex;
    flex-direction: column;
    font-weight: 500;
    color: #444;
  }
  input,
  textarea {
    margin-top: 0.5rem;
    padding: 0.7rem;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 0.5rem;
  }
  button {
    padding: 0.8rem;
    font-size: 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 0.5rem;
    cursor: pointer;
    transition: background-color 0.2s ease;
  }
  button:hover {
    background-color: #0056b3;
  }
  .status {
    text-align: center;
    margin-top: 1rem;
    font-weight: bold;
  }
  .success {
    color: green;
  }
  .error {
    color: red;
  }
</style>
