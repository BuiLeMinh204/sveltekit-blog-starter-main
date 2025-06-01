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
        headers: { "Content-Type": "application/json" },
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

<form on:submit|preventDefault={sendEmail} class="form">
  <label>
    To:
    <input type="email" bind:value={to} required />
  </label>
  <label>
    Subject:
    <input type="text" bind:value={subject} required />
  </label>
  <label>
    Body:
    <textarea bind:value={body} required></textarea>
  </label>
  <button type="submit">Send Email</button>
</form>

{#if success}
  <p class="success">✅ Email has been queued.</p>
{:else if error}
  <p class="error">❌ {error}</p>
{/if}

<style>
  .form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 400px;
    margin: 2rem auto;
  }
  input, textarea {
    padding: 0.5rem;
    font-size: 1rem;
    width: 100%;
  }
  .success {
    color: green;
    text-align: center;
  }
  .error {
    color: red;
    text-align: center;
  }
</style>
