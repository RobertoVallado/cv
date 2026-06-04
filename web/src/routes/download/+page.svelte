<script lang="ts">
  import { onMount } from 'svelte';
  import { browser } from '$app/environment';
  import { locale } from '$lib/i18n';

  let loading = true;
  let error = false;

  onMount(async () => {
    if (browser) {
      try {
        const lang = $locale === 'fr' ? 'fr' : 'en';
        const pdfUrl = `/roberto-vallado-cv-${lang}.pdf`;
        const response = await fetch(pdfUrl, { method: 'HEAD' });
        if (response.ok) {
          window.location.href = pdfUrl;
        } else {
          throw new Error('PDF not found');
        }
      } catch (err) {
        console.error('Download error:', err);
        error = true;
        loading = false;
      }
    }
  });
</script>

<svelte:head>
  <title>{$locale === 'fr' ? 'Téléchargement du CV...' : 'Downloading CV...'}</title>
  <meta name="robots" content="noindex" />
</svelte:head>

{#if loading && !error}
  <div class="loading">
    <h1>{$locale === 'fr' ? 'Téléchargement en cours...' : 'Downloading CV...'}</h1>
    <p>{$locale === 'fr' ? 'Votre téléchargement devrait démarrer automatiquement.' : 'Your download should start automatically.'}</p>
  </div>
{:else if error}
  <div class="error">
    <h1>{$locale === 'fr' ? 'Erreur de téléchargement' : 'Download Error'}</h1>
    <p>{$locale === 'fr' ? 'Le PDF est introuvable. Vous pouvez :' : 'Sorry, the PDF could not be found. You can:'}</p>
    <ul>
      <li><a href="https://github.com/RobertoVallado/cv" target="_blank" rel="noopener">
        {$locale === 'fr' ? 'Visiter le dépôt GitHub' : 'Visit the GitHub repo'}
      </a></li>
      <li><a href="/">{$locale === 'fr' ? 'Retourner au site' : 'Return to the CV website'}</a></li>
    </ul>
  </div>
{/if}

<style>
  .loading, .error {
    text-align: center;
    padding: 2rem;
    max-width: 600px;
    margin: 2rem auto;
  }
  .error ul { list-style: none; padding: 0; }
  .error li { margin: 1rem 0; }
  .error a { color: var(--primary); text-decoration: none; }
  .error a:hover { text-decoration: underline; }
</style>
